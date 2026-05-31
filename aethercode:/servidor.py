import http.server
import socketserver
import urllib.parse
import paginas
import bd
import ejercicios

PORT = 8000

# Sesión simple en memoria: guarda el estudiante activo
sesion = {}

class Manejador(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            ruta = self.path.split('?')[0]
            params = urllib.parse.parse_qs(
                self.path.split('?')[1] if '?' in self.path else ''
            )

            # Rutas que no requieren login
            if ruta == '/login':
                html = paginas.pagina_login()
            elif ruta == '/registro':
                html = paginas.pagina_registro()

            # Todo lo demás requiere estar logueado
            elif 'id_estudiante' not in sesion:
                html = paginas.pagina_login(mensaje="Debes iniciar sesión primero.")

            elif ruta == '/':
                est = bd.get_estudiante(sesion['id_estudiante'])
                puntaje = bd.get_puntaje(sesion['id_estudiante'])
                html = paginas.pagina_inicio(est, puntaje)

            elif ruta == '/lenguajes':
                est = bd.get_estudiante(sesion['id_estudiante'])
                lenguajes = bd.get_lenguajes()
                html = paginas.pagina_lenguajes(est, lenguajes)

            elif ruta == '/temas':
                id_lang = int(params.get('lang', [1])[0])
                lenguaje = bd.get_lenguaje(id_lang)
                temas = bd.get_temas(id_lang)
                est = bd.get_estudiante(sesion['id_estudiante'])
                html = paginas.pagina_temas(est, lenguaje, temas)

            elif ruta == '/ejercicio':
                id_tema = int(params.get('tema', [1])[0])
                dificultad = params.get('dificultad', ['todos'])[0]
                idx = int(params.get('idx', [0])[0])
                lista = bd.get_ejercicios(id_tema, dificultad)
                if not lista or idx >= len(lista):
                    html = paginas.pagina_404()
                else:
                    ejercicio = lista[idx]
                    tema = bd.get_tema(id_tema)
                    puntaje = bd.get_puntaje(sesion['id_estudiante'])
                    html = paginas.pagina_ejercicio(
                        ejercicio, tema, dificultad, idx, len(lista), puntaje
                    )

            elif ruta == '/historial':
                est = bd.get_estudiante(sesion['id_estudiante'])
                historial = bd.get_historial(sesion['id_estudiante'])
                html = paginas.pagina_historial(est, historial)

            elif ruta == '/ranking':
                ranking = bd.get_ranking()
                est = bd.get_estudiante(sesion['id_estudiante'])
                html = paginas.pagina_ranking(est, ranking)

            elif ruta == '/resumen':
                est = bd.get_estudiante(sesion['id_estudiante'])
                datos = bd.get_resumen(sesion['id_estudiante'])
                puntaje = bd.get_puntaje(sesion['id_estudiante'])
                html = paginas.pagina_resumen(est, datos, puntaje)

            elif ruta == '/logout':
                sesion.clear()
                html = paginas.pagina_login(mensaje="Sesión cerrada correctamente.")

            else:
                html = paginas.pagina_404()

            self._enviar(html)

        except Exception as e:
            self._enviar(f"<h1>Error interno</h1><p>{str(e)}</p>")

    def do_POST(self):
        try:
            largo = int(self.headers['Content-Length'])
            datos = self.rfile.read(largo).decode('utf-8')
            params = urllib.parse.parse_qs(datos)
            ruta = self.path

            if ruta == '/login':
                nombre = params.get('nombre', [''])[0].strip()
                contrasena = params.get('contrasena', [''])[0]
                est = bd.login_estudiante(nombre, contrasena)
                if est:
                    sesion['id_estudiante'] = est['id']
                    puntaje = bd.get_puntaje(est['id'])
                    html = paginas.pagina_inicio(est, puntaje)
                else:
                    html = paginas.pagina_login(
                        mensaje="Nombre o contraseña incorrectos."
                    )

            elif ruta == '/registro':
                nombre = params.get('nombre', [''])[0].strip()
                contrasena = params.get('contrasena', [''])[0]
                if len(nombre) < 3:
                    html = paginas.pagina_registro(
                        mensaje="El nombre debe tener al menos 3 caracteres."
                    )
                elif len(contrasena) < 4:
                    html = paginas.pagina_registro(
                        mensaje="La contraseña debe tener al menos 4 caracteres."
                    )
                else:
                    ok = bd.registrar_estudiante(nombre, contrasena)
                    if ok:
                        est = bd.login_estudiante(nombre, contrasena)
                        sesion['id_estudiante'] = est['id']
                        puntaje = bd.get_puntaje(est['id'])
                        html = paginas.pagina_inicio(est, puntaje)
                    else:
                        html = paginas.pagina_registro(
                            mensaje="Ese nombre de usuario ya existe."
                        )

            elif ruta == '/responder':
                if 'id_estudiante' not in sesion:
                    html = paginas.pagina_login()
                elif 'respuesta' not in params:
                    id_tema   = int(params.get('id_tema', [1])[0])
                    dificultad = params.get('dificultad', ['todos'])[0]
                    idx       = int(params.get('idx', [0])[0])
                    html = paginas.pagina_error(
                        "Debes seleccionar una opción antes de responder.",
                        f"/ejercicio?tema={id_tema}&dificultad={dificultad}&idx={idx}"
                    )
                else:
                    id_ej      = int(params['id_ejercicio'][0])
                    id_tema    = int(params['id_tema'][0])
                    dificultad = params['dificultad'][0]
                    idx        = int(params['idx'][0])
                    respuesta  = params['respuesta'][0]
                    tiempo     = int(params.get('tiempo', [15])[0])

                    correcto = ejercicios.validar(id_ej, respuesta)
                    mensaje  = ejercicios.get_mensaje(id_ej, correcto)
                    puntos   = bd.guardar_intento(
                        sesion['id_estudiante'], id_ej,
                        respuesta, correcto, tiempo
                    )
                    puntaje  = bd.get_puntaje(sesion['id_estudiante'])

                    lista    = bd.get_ejercicios(id_tema, dificultad)
                    siguiente = idx + 1 if idx + 1 < len(lista) else None

                    html = paginas.pagina_resultado(
                        correcto, mensaje, puntos, puntaje,
                        id_tema, dificultad, idx, siguiente
                    )
            else:
                html = paginas.pagina_404()

            self._enviar(html)

        except Exception as e:
            self._enviar(f"<h1>Error interno</h1><p>{str(e)}</p>")

    def _enviar(self, html):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def log_message(self, *args):
        pass

bd.inicializar()
print(f'Servidor en http://localhost:{PORT}')

with socketserver.TCPServer(('', PORT), Manejador) as s:
    s.serve_forever()