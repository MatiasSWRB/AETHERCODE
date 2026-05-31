def base(titulo, contenido, est=None, puntaje=None):
    nav_usuario = ''
    if est:
        racha  = puntaje['racha_actual']  if puntaje else 0
        puntos = puntaje['puntos_total']  if puntaje else 0
        nav_usuario = f'''
        <div class="nav-user">
            <span class="nav-stat">{racha} RACHA</span>
            <span class="nav-stat">{puntos} PTS</span>
            <span class="nav-nombre">{est["nombre"]}</span>
            <a href="/logout" class="nav-logout">SALIR</a>
        </div>'''
    else:
        nav_usuario = '''
        <div class="nav-user">
            <a href="/login" class="btn-outline">INICIAR SESION</a>
            <a href="/registro" class="btn-primary">REGISTRARSE</a>
        </div>'''

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo} — AETHERCODE</title>
<style>
  :root {{
    --negro:      #0A0A0A;
    --negro-card: #111111;
    --negro-mid:  #1A1A1A;
    --borde:      #2A2A2A;
    --blanco:     #F5F5F0;
    --blanco-mid: #CCCCCC;
    --gris:       #666666;
    --acento:     #E8E0D0;
    --rojo:       #C0392B;
    --verde:      #27AE60;
  }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}

  html {{ scroll-behavior: smooth; }}

  body {{
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    background: var(--negro);
    color: var(--blanco);
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
  }}

  /* ── NAV ── */
  nav {{
    background: var(--negro);
    border-bottom: 1px solid var(--borde);
    padding: 0 4rem;
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
  }}

  .nav-logo {{
    font-size: .75rem;
    font-weight: 800;
    letter-spacing: 6px;
    text-transform: uppercase;
    color: var(--blanco);
    text-decoration: none;
  }}

  .nav-links {{
    display: flex;
    gap: 3rem;
  }}

  .nav-links a {{
    color: var(--gris);
    text-decoration: none;
    font-size: .7rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    transition: color .15s;
  }}

  .nav-links a:hover {{ color: var(--blanco); }}

  .nav-user {{
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }}

  .nav-stat {{
    font-size: .65rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--gris);
    border: 1px solid var(--borde);
    padding: .3rem .8rem;
  }}

  .nav-nombre {{
    font-size: .7rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--blanco);
  }}

  .nav-logout {{
    font-size: .65rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--gris);
    text-decoration: none;
    border: 1px solid var(--borde);
    padding: .3rem .8rem;
    transition: all .15s;
  }}

  .nav-logout:hover {{
    border-color: var(--blanco);
    color: var(--blanco);
  }}

  /* ── LAYOUT ── */
  .container {{
    max-width: 1140px;
    margin: 0 auto;
    padding: 4rem 2rem;
  }}

  /* ── SECCION TITULO ── */
  .section-label {{
    font-size: .65rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--gris);
    margin-bottom: 1rem;
    display: block;
  }}

  /* ── TIPOGRAFIA ── */
  h1 {{
    font-size: 4rem;
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1;
    color: var(--blanco);
    text-transform: uppercase;
    margin-bottom: 1.5rem;
  }}

  h2 {{
    font-size: 1.8rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: var(--blanco);
    text-transform: uppercase;
    margin-bottom: .8rem;
  }}

  h3 {{
    font-size: .65rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--gris);
    margin-bottom: .5rem;
  }}

  p {{
    font-size: .95rem;
    line-height: 1.8;
    color: var(--blanco-mid);
  }}

  /* ── CARDS ── */
  .card {{
    background: var(--negro-card);
    border: 1px solid var(--borde);
    padding: 2.5rem;
    margin-bottom: 1.5rem;
  }}

  .card-blanco {{
    background: var(--blanco);
    color: var(--negro);
    border: none;
  }}

  .card-blanco h1,
  .card-blanco h2,
  .card-blanco h3,
  .card-blanco p {{
    color: var(--negro);
  }}

  .card-blanco h3 {{
    color: var(--gris);
  }}

  /* ── BOTONES ── */
  .btn-primary {{
    display: inline-block;
    background: var(--blanco);
    color: var(--negro);
    padding: .75rem 2.5rem;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: opacity .15s;
  }}

  .btn-primary:hover {{ opacity: .85; }}

  .btn-outline {{
    display: inline-block;
    background: transparent;
    color: var(--blanco);
    padding: .75rem 2.5rem;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-decoration: none;
    border: 1px solid var(--borde);
    cursor: pointer;
    transition: border-color .15s;
  }}

  .btn-outline:hover {{ border-color: var(--blanco); }}

  .btn-negro {{
    display: inline-block;
    background: var(--negro);
    color: var(--blanco);
    padding: .75rem 2.5rem;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: opacity .15s;
  }}

  .btn-negro:hover {{ opacity: .8; }}

  /* ── GRID ── */
  .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; }}
  .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; }}
  .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; }}

  @media (max-width: 768px) {{
    .grid-2, .grid-3, .grid-4 {{ grid-template-columns: 1fr; gap: 1px; }}
    h1 {{ font-size: 2.5rem; }}
    nav {{ padding: 0 1.5rem; }}
    .nav-links {{ display: none; }}
    .container {{ padding: 2rem 1.5rem; }}
  }}

  /* ── STAT ── */
  .stat {{
    background: var(--negro-card);
    border: 1px solid var(--borde);
    padding: 2rem;
    text-align: center;
  }}

  .stat-num {{
    display: block;
    font-size: 3rem;
    font-weight: 900;
    color: var(--blanco);
    line-height: 1;
    margin-bottom: .5rem;
    letter-spacing: -2px;
  }}

  .stat-label {{
    font-size: .6rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gris);
  }}

  /* ── FORMULARIOS ── */
  .form-group {{ margin-bottom: 1.5rem; }}

  .form-group label {{
    display: block;
    font-size: .65rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gris);
    margin-bottom: .6rem;
  }}

  .form-group input {{
    width: 100%;
    padding: .85rem 1rem;
    background: var(--negro-mid);
    border: 1px solid var(--borde);
    color: var(--blanco);
    font-family: inherit;
    font-size: .95rem;
    outline: none;
    transition: border-color .15s;
  }}

  .form-group input:focus {{ border-color: var(--blanco); }}

  .form-group input::placeholder {{ color: var(--gris); }}

  /* ── OPCIONES EJERCICIO ── */
  .opcion {{
    display: block;
    width: 100%;
    text-align: left;
    background: var(--negro-mid);
    border: 1px solid var(--borde);
    padding: 1.2rem 1.5rem;
    margin-bottom: .6rem;
    cursor: pointer;
    font-family: inherit;
    font-size: .9rem;
    color: var(--blanco-mid);
    transition: all .15s;
    letter-spacing: .5px;
  }}

  .opcion:hover {{
    background: var(--negro-card);
    border-color: var(--blanco);
    color: var(--blanco);
  }}

  .opcion-activa {{
    border-color: var(--blanco) !important;
    color: var(--blanco) !important;
    background: var(--negro-card) !important;
  }}

  /* ── BARRA PROGRESO ── */
  .barra-wrap {{
    background: var(--negro-mid);
    height: 2px;
    margin: .8rem 0 2rem;
    position: relative;
  }}

  .barra-fill {{
    height: 100%;
    background: var(--blanco);
    transition: width .4s ease;
  }}

  /* ── TEMPORIZADOR ── */
  .timer-bloque {{
    display: flex;
    align-items: baseline;
    gap: .5rem;
  }}

  .timer-num {{
    font-size: 3rem;
    font-weight: 900;
    color: var(--blanco);
    letter-spacing: -2px;
    line-height: 1;
  }}

  .timer-label {{
    font-size: .6rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gris);
  }}

  /* ── BADGE DIFICULTAD ── */
  .badge {{
    display: inline-block;
    padding: .2rem .8rem;
    font-size: .6rem;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    border: 1px solid;
  }}

  .badge-facil   {{ border-color: var(--verde); color: var(--verde); }}
  .badge-medio   {{ border-color: #F39C12; color: #F39C12; }}
  .badge-dificil {{ border-color: var(--rojo); color: var(--rojo); }}

  /* ── RESULTADO ── */
  .borde-correcto   {{ border-left: 3px solid var(--verde); }}
  .borde-incorrecto {{ border-left: 3px solid var(--rojo); }}

  /* ── TABLA ── */
  table {{
    width: 100%;
    border-collapse: collapse;
    border: 1px solid var(--borde);
  }}

  th {{
    background: var(--negro-mid);
    color: var(--gris);
    padding: .8rem 1.2rem;
    text-align: left;
    font-size: .6rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    border-bottom: 1px solid var(--borde);
    font-weight: 700;
  }}

  td {{
    padding: .9rem 1.2rem;
    border-bottom: 1px solid var(--borde);
    font-size: .85rem;
    color: var(--blanco-mid);
  }}

  tr:last-child td {{ border-bottom: none; }}

  tr:hover td {{
    background: var(--negro-mid);
    color: var(--blanco);
  }}

  /* ── DIVISOR ── */
  .divisor {{
    border: none;
    border-top: 1px solid var(--borde);
    margin: 2rem 0;
  }}

  /* ── MENSAJE ── */
  .msg-error {{
    background: transparent;
    border: 1px solid var(--rojo);
    color: var(--rojo);
    padding: .8rem 1.2rem;
    font-size: .8rem;
    letter-spacing: 1px;
    margin-bottom: 1.5rem;
  }}

  /* ── LANG / TEMA CARD ── */
  .item-card {{
    background: var(--negro-card);
    border: 1px solid var(--borde);
    padding: 2rem;
    text-decoration: none;
    color: var(--blanco);
    display: block;
    transition: border-color .15s;
    position: relative;
    overflow: hidden;
  }}

  .item-card:hover {{
    border-color: var(--blanco);
  }}

  .item-card:hover .item-arrow {{
    opacity: 1;
    transform: translateX(0);
  }}

  .item-lang {{
    font-size: .6rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--gris);
    margin-bottom: .8rem;
    display: block;
  }}

  .item-nombre {{
    font-size: 1.4rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: -0.5px;
    color: var(--blanco);
  }}

  .item-sub {{
    font-size: .65rem;
    color: var(--gris);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: .8rem;
    display: block;
  }}

  .item-arrow {{
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateX(8px) translateY(-50%);
    opacity: 0;
    transition: all .2s;
    font-size: 1.2rem;
    color: var(--blanco);
  }}

  /* ── RANKING ── */
  .rank-pos {{
    font-size: 1.4rem;
    font-weight: 900;
    letter-spacing: -1px;
    color: var(--gris);
  }}

  .rank-1 {{ color: var(--blanco); }}
  .rank-2 {{ color: #AAAAAA; }}
  .rank-3 {{ color: #666666; }}

  /* ── LINEA DECORATIVA ── */
  .linea {{
    width: 40px;
    height: 2px;
    background: var(--blanco);
    margin-bottom: 1.5rem;
  }}

  /* ── FOOTER ── */
  .footer {{
    border-top: 1px solid var(--borde);
    padding: 2rem;
    text-align: center;
    font-size: .6rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--gris);
  }}
</style>
</head>
<body>
<nav>
  <a href="/" class="nav-logo">Aether&nbsp;Code</a>
  <div class="nav-links">
    <a href="/lenguajes">Lenguajes</a>
    <a href="/historial">Historial</a>
    <a href="/ranking">Ranking</a>
    <a href="/resumen">Resumen</a>
  </div>
  {nav_usuario}
</nav>

<div class="container">
  {contenido}
  <div class="footer">Universidad Tecnica de Ambato &nbsp;&middot;&nbsp; Algoritmos y Programacion &nbsp;&middot;&nbsp; 2026</div>
</div>
</body>
</html>'''


# ── LOGIN ──────────────────────────────────────────────────────────────────
def pagina_login(mensaje=''):
    msg_html = f'<div class="msg-error">{mensaje}</div>' if mensaje else ''
    contenido = f'''
<div style="display:grid; grid-template-columns:1fr 1fr; min-height:80vh; gap:1px; margin:-4rem -2rem;">

  <div style="background:var(--negro-card); border-right:1px solid var(--borde);
              display:flex; flex-direction:column; justify-content:center; padding:5rem;">
    <span class="section-label">Plataforma educativa</span>
    <div class="linea"></div>
    <h1 style="font-size:3.5rem;">AETHER<br>CODE</h1>
    <p style="margin-top:1.5rem; max-width:320px;">
      Aprende algoritmos y programacion mediante ejercicios interactivos
      con retroalimentacion inmediata.
    </p>
    <div style="margin-top:3rem; border-top:1px solid var(--borde); padding-top:2rem;">
      <div style="display:flex; gap:3rem;">
        <div>
          <span style="display:block; font-size:1.8rem; font-weight:900; letter-spacing:-1px;">250</span>
          <span style="font-size:.6rem; letter-spacing:3px; text-transform:uppercase; color:var(--gris);">Ejercicios</span>
        </div>
        <div>
          <span style="display:block; font-size:1.8rem; font-weight:900; letter-spacing:-1px;">5</span>
          <span style="font-size:.6rem; letter-spacing:3px; text-transform:uppercase; color:var(--gris);">Lenguajes</span>
        </div>
        <div>
          <span style="display:block; font-size:1.8rem; font-weight:900; letter-spacing:-1px;">25</span>
          <span style="font-size:.6rem; letter-spacing:3px; text-transform:uppercase; color:var(--gris);">Temas</span>
        </div>
      </div>
    </div>
  </div>

  <div style="display:flex; flex-direction:column; justify-content:center; padding:5rem;">
    <span class="section-label">Acceso</span>
    <h2 style="margin-bottom:2rem;">Iniciar sesion</h2>
    {msg_html}
    <form method="post" action="/login">
      <div class="form-group">
        <label>Usuario</label>
        <input type="text" name="nombre" placeholder="Tu nombre de usuario" required autofocus>
      </div>
      <div class="form-group">
        <label>Contrasena</label>
        <input type="password" name="contrasena" placeholder="••••••••" required>
      </div>
      <button type="submit" class="btn-primary" style="width:100%; margin-top:.5rem;">
        Ingresar
      </button>
    </form>
    <hr class="divisor">
    <p style="font-size:.8rem; color:var(--gris);">
      Sin cuenta —
      <a href="/registro" style="color:var(--blanco); font-weight:700; text-decoration:none;">
        Registrarse
      </a>
    </p>
  </div>

</div>'''
    return base('Iniciar sesion', contenido)


# ── REGISTRO ───────────────────────────────────────────────────────────────
def pagina_registro(mensaje=''):
    msg_html = f'<div class="msg-error">{mensaje}</div>' if mensaje else ''
    contenido = f'''
<div style="display:grid; grid-template-columns:1fr 1fr; min-height:80vh; gap:1px; margin:-4rem -2rem;">

  <div style="background:var(--negro-card); border-right:1px solid var(--borde);
              display:flex; flex-direction:column; justify-content:center; padding:5rem;">
    <span class="section-label">Nuevo estudiante</span>
    <div class="linea"></div>
    <h1 style="font-size:3.5rem;">CREA TU<br>CUENTA</h1>
    <p style="margin-top:1.5rem; max-width:320px;">
      Registrate para guardar tu progreso, acumular puntos
      y competir en el ranking global.
    </p>
  </div>

  <div style="display:flex; flex-direction:column; justify-content:center; padding:5rem;">
    <span class="section-label">Registro</span>
    <h2 style="margin-bottom:2rem;">Crear cuenta</h2>
    {msg_html}
    <form method="post" action="/registro">
      <div class="form-group">
        <label>Nombre de usuario</label>
        <input type="text" name="nombre" placeholder="Minimo 3 caracteres" required autofocus>
      </div>
      <div class="form-group">
        <label>Contrasena</label>
        <input type="password" name="contrasena" placeholder="Minimo 4 caracteres" required>
      </div>
      <button type="submit" class="btn-primary" style="width:100%; margin-top:.5rem;">
        Crear cuenta
      </button>
    </form>
    <hr class="divisor">
    <p style="font-size:.8rem; color:var(--gris);">
      Ya tienes cuenta —
      <a href="/login" style="color:var(--blanco); font-weight:700; text-decoration:none;">
        Iniciar sesion
      </a>
    </p>
  </div>

</div>'''
    return base('Registro', contenido)


# ── INICIO ─────────────────────────────────────────────────────────────────
def pagina_inicio(est, puntaje):
    puntos       = puntaje['puntos_total']  if puntaje else 0
    racha        = puntaje['racha_actual']  if puntaje else 0
    mejor_racha  = puntaje['mejor_racha']   if puntaje else 0
    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:3rem; margin-bottom:3rem;">
  <span class="section-label">Panel principal</span>
  <div class="linea"></div>
  <h1 style="font-size:5rem;">{est["nombre"].upper()}</h1>
  <p style="max-width:500px; margin-bottom:2rem;">
    Continua donde lo dejaste. Cada ejercicio resuelto suma puntos
    y sube tu posicion en el ranking.
  </p>
  <div style="display:flex; gap:1rem;">
    <a href="/lenguajes" class="btn-primary">Practicar ahora</a>
    <a href="/resumen" class="btn-outline">Ver progreso</a>
  </div>
</div>

<div class="grid-3" style="margin-bottom:3rem; border:1px solid var(--borde);">
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{puntos}</span>
    <span class="stat-label">Puntos totales</span>
  </div>
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{racha}</span>
    <span class="stat-label">Racha actual</span>
  </div>
  <div class="stat" style="border:none;">
    <span class="stat-num">{mejor_racha}</span>
    <span class="stat-label">Mejor racha</span>
  </div>
</div>

<div class="grid-2" style="gap:1.5rem;">
  <div class="card" style="margin:0;">
    <h3>Contenido</h3>
    <h2 style="font-size:1.4rem; margin-bottom:.5rem;">5 Lenguajes</h2>
    <p style="font-size:.85rem; color:var(--gris);">
      Python — JavaScript — Java — C++ — SQL
    </p>
    <br>
    <a href="/lenguajes" class="btn-outline">Explorar</a>
  </div>
  <div class="card" style="margin:0;">
    <h3>Competencia</h3>
    <h2 style="font-size:1.4rem; margin-bottom:.5rem;">Ranking global</h2>
    <p style="font-size:.85rem; color:var(--gris);">
      Compite con otros estudiantes. Los puntos se acumulan por velocidad y precision.
    </p>
    <br>
    <a href="/ranking" class="btn-outline">Ver ranking</a>
  </div>
</div>'''
    return base('Inicio', contenido, est, puntaje)


# ── LENGUAJES ──────────────────────────────────────────────────────────────
ICONOS = {
    'Python': 'PY', 'JavaScript': 'JS',
    'Java': 'JV', 'C++': 'C+', 'SQL': 'SQ'
}

def pagina_lenguajes(est, lenguajes):
    cards = ''
    for l in lenguajes:
        sigla = ICONOS.get(l['nombre'], '--')
        cards += f'''
<a href="/temas?lang={l['id']}" class="item-card">
  <span style="font-size:2rem; font-weight:900; letter-spacing:-1px;
               color:var(--borde); display:block; margin-bottom:1rem;">{sigla}</span>
  <span class="item-lang">Lenguaje</span>
  <span class="item-nombre">{l['nombre']}</span>
  <span class="item-sub">5 temas &nbsp;&middot;&nbsp; 50 ejercicios</span>
  <span class="item-arrow">&#8594;</span>
</a>'''

    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:2rem; margin-bottom:3rem;">
  <span class="section-label">Seleccion</span>
  <div class="linea"></div>
  <h1>Lenguajes</h1>
  <p>Elige el lenguaje que quieres practicar hoy.</p>
</div>
<div class="grid-3" style="gap:1.5rem;">{cards}</div>'''
    return base('Lenguajes', contenido, est)


# ── TEMAS ──────────────────────────────────────────────────────────────────
def pagina_temas(est, lenguaje, temas):
    sigla = ICONOS.get(lenguaje['nombre'], '--')
    cards = ''
    for i, t in enumerate(temas):
        num = str(i + 1).zfill(2)
        cards += f'''
<a href="/ejercicio?tema={t['id']}&dificultad=todos&idx=0" class="item-card">
  <span style="font-size:2.5rem; font-weight:900; letter-spacing:-2px;
               color:var(--borde); display:block; margin-bottom:.8rem;">{num}</span>
  <span class="item-lang">{lenguaje['nombre']}</span>
  <span class="item-nombre" style="font-size:1.1rem;">{t['nombre']}</span>
  <span class="item-sub">10 ejercicios &nbsp;&middot;&nbsp; Facil / Medio / Dificil</span>
  <span class="item-arrow">&#8594;</span>
</a>'''

    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:2rem; margin-bottom:3rem;">
  <a href="/lenguajes" style="font-size:.65rem; font-weight:700; letter-spacing:3px;
     text-transform:uppercase; color:var(--gris); text-decoration:none;">
    &larr; Lenguajes
  </a>
  <div style="margin-top:1.5rem;">
    <span class="section-label">{sigla} — {lenguaje['nombre']}</span>
    <div class="linea"></div>
    <h1>Temas</h1>
  </div>
</div>
<div class="grid-2" style="gap:1.5rem;">{cards}</div>

<div class="card" style="margin-top:2rem;">
  <h3>Dificultad</h3>
  <div style="display:flex; gap:1.5rem; margin-top:1rem; flex-wrap:wrap;">
    <div>
      <span class="badge badge-facil">Facil</span>
      <p style="font-size:.8rem; margin-top:.4rem; color:var(--gris);">Conceptos base</p>
    </div>
    <div>
      <span class="badge badge-medio">Medio</span>
      <p style="font-size:.8rem; margin-top:.4rem; color:var(--gris);">Aplicacion practica</p>
    </div>
    <div>
      <span class="badge badge-dificil">Dificil</span>
      <p style="font-size:.8rem; margin-top:.4rem; color:var(--gris);">Dominio avanzado</p>
    </div>
  </div>
</div>'''
    return base(lenguaje['nombre'], contenido, est)


# ── EJERCICIO ──────────────────────────────────────────────────────────────
def pagina_ejercicio(ejercicio, tema, dificultad, idx, total, puntaje):
    progreso   = int((idx / total) * 100)
    badge_cls  = f"badge-{ejercicio['dificultad']}"
    puntos_act = puntaje['puntos_total'] if puntaje else 0
    racha_act  = puntaje['racha_actual'] if puntaje else 0
    num        = str(idx + 1).zfill(2)

    contenido = f'''
<div style="display:flex; justify-content:space-between; align-items:flex-start;
            border-bottom:1px solid var(--borde); padding-bottom:1.5rem; margin-bottom:2rem; flex-wrap:wrap; gap:1rem;">
  <div>
    <a href="/temas?lang=0" style="font-size:.65rem; font-weight:700; letter-spacing:3px;
       text-transform:uppercase; color:var(--gris); text-decoration:none;">&larr; Temas</a>
    <div style="margin-top:.8rem; display:flex; align-items:center; gap:1rem;">
      <span class="badge {badge_cls}">{ejercicio['dificultad']}</span>
      <span style="font-size:.65rem; font-weight:700; letter-spacing:3px;
                   text-transform:uppercase; color:var(--gris);">{tema['nombre']}</span>
    </div>
  </div>
  <div style="text-align:right;">
    <span style="font-size:.65rem; font-weight:700; letter-spacing:3px;
                 text-transform:uppercase; color:var(--gris); display:block;">{puntos_act} pts &nbsp; {racha_act} racha</span>
    <div class="timer-bloque" style="justify-content:flex-end; margin-top:.3rem;">
      <span class="timer-num" id="timer">30</span>
      <span class="timer-label">seg</span>
    </div>
  </div>
</div>

<div style="display:flex; gap:3rem; align-items:flex-start; flex-wrap:wrap;">

  <div style="flex:1; min-width:280px;">
    <div style="margin-bottom:2rem;">
      <span style="font-size:4rem; font-weight:900; letter-spacing:-3px;
                   color:var(--borde); display:block; line-height:1;">{num}</span>
      <span style="font-size:.6rem; font-weight:700; letter-spacing:3px;
                   text-transform:uppercase; color:var(--gris);">de {str(total).zfill(2)}</span>
    </div>

    <div class="barra-wrap">
      <div class="barra-fill" style="width:{progreso}%;"></div>
    </div>

    <p style="font-size:1.15rem; font-weight:600; color:var(--blanco);
              line-height:1.6; margin-bottom:2.5rem;">
      {ejercicio['pregunta']}
    </p>
  </div>

  <div style="flex:1; min-width:280px;">
    <form method="post" action="/responder" id="form-ej">
      <input type="hidden" name="id_ejercicio" value="{ejercicio['id']}">
      <input type="hidden" name="id_tema"      value="{tema['id']}">
      <input type="hidden" name="dificultad"   value="{dificultad}">
      <input type="hidden" name="idx"          value="{idx}">
      <input type="hidden" name="tiempo"       id="tiempo-input" value="30">
      <input type="hidden" name="respuesta"    id="respuesta-input" value="">

      <button type="button" class="opcion" id="op-a" onclick="elegir('a', this)">
        {ejercicio['opcion_a']}
      </button>
      <button type="button" class="opcion" id="op-b" onclick="elegir('b', this)">
        {ejercicio['opcion_b']}
      </button>
      <button type="button" class="opcion" id="op-c" onclick="elegir('c', this)">
        {ejercicio['opcion_c']}
      </button>

      <button type="submit" class="btn-primary" id="btn-responder"
              disabled style="width:100%; margin-top:1rem; opacity:.3; cursor:not-allowed;">
        Selecciona una opcion
      </button>
    </form>
  </div>

</div>

<script>
  let seg = 30, transcurrido = 0;
  const timerEl = document.getElementById('timer');
  const tInput  = document.getElementById('tiempo-input');

  const iv = setInterval(() => {{
    seg--; transcurrido++;
    timerEl.textContent = seg;
    if (seg <= 10) timerEl.style.color = '#C0392B';
    if (seg <= 0) {{
      clearInterval(iv);
      tInput.value = 30;
      document.getElementById('form-ej').submit();
    }}
  }}, 1000);

  function elegir(val, btn) {{
    ['a','b','c'].forEach(x => {{
      const b = document.getElementById('op-' + x);
      b.classList.remove('opcion-activa');
    }});
    btn.classList.add('opcion-activa');
    document.getElementById('respuesta-input').value = val;
    tInput.value = transcurrido;
    const r = document.getElementById('btn-responder');
    r.disabled = false;
    r.style.opacity = '1';
    r.style.cursor  = 'pointer';
    r.textContent   = 'Confirmar respuesta';
  }}
</script>'''
    return base(f'Ejercicio {idx+1}', contenido, None, puntaje)


# ── RESULTADO ──────────────────────────────────────────────────────────────
def pagina_resultado(correcto, mensaje, puntos_ganados, puntaje,
                     id_tema, dificultad, idx, siguiente):
    borde_cls = 'borde-correcto' if correcto else 'borde-incorrecto'
    estado    = 'CORRECTO' if correcto else 'INCORRECTO'
    color_est = 'var(--verde)' if correcto else 'var(--rojo)'
    pt_total  = puntaje['puntos_total'] if puntaje else 0
    racha     = puntaje['racha_actual'] if puntaje else 0

    if siguiente is not None:
        boton_sig = f'<a href="/ejercicio?tema={id_tema}&dificultad={dificultad}&idx={siguiente}" class="btn-primary">Siguiente ejercicio</a>'
    else:
        boton_sig = '<a href="/resumen" class="btn-primary">Ver resumen final</a>'

    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:2rem; margin-bottom:2rem;">
  <span class="section-label">Resultado</span>
  <div class="linea" style="background:{color_est};"></div>
  <h1 style="color:{color_est}; font-size:5rem;">{estado}</h1>
</div>

<div class="card {borde_cls}" style="margin-bottom:2rem;">
  <p style="font-size:1rem; color:var(--blanco-mid); line-height:1.7;">{mensaje}</p>
</div>

<div class="grid-3" style="border:1px solid var(--borde); margin-bottom:2rem;">
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num" style="color:{'var(--verde)' if correcto else 'var(--gris)'};">+{puntos_ganados}</span>
    <span class="stat-label">Puntos ganados</span>
  </div>
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{pt_total}</span>
    <span class="stat-label">Total acumulado</span>
  </div>
  <div class="stat" style="border:none;">
    <span class="stat-num">{racha}</span>
    <span class="stat-label">Racha actual</span>
  </div>
</div>

<div style="display:flex; gap:1rem; flex-wrap:wrap;">
  {boton_sig}
  <a href="/ejercicio?tema={id_tema}&dificultad={dificultad}&idx={idx}" class="btn-outline">Reintentar</a>
  <a href="/lenguajes" class="btn-outline">Cambiar tema</a>
</div>'''
    return base('Resultado', contenido, None, puntaje)


# ── HISTORIAL ──────────────────────────────────────────────────────────────
def pagina_historial(est, historial):
    if not historial:
        cuerpo = '''
<div class="card">
  <p style="color:var(--gris);">Sin intentos registrados aun.</p>
  <br>
  <a href="/lenguajes" class="btn-primary">Ir a ejercicios</a>
</div>'''
    else:
        correctos  = sum(1 for i in historial if i['correcto'])
        porcentaje = int((correctos / len(historial)) * 100)
        filas = ''.join(f'''
<tr>
  <td><span class="badge badge-{i['dificultad']}">{i['dificultad']}</span></td>
  <td style="font-weight:600; color:var(--blanco);">{i['lenguaje']}</td>
  <td>{i['tema']}</td>
  <td style="font-family:monospace;">{i['respuesta'].upper()}</td>
  <td style="color:{'var(--verde)' if i['correcto'] else 'var(--rojo)'}; font-weight:700;">
    {'OK' if i['correcto'] else 'FAIL'}
  </td>
  <td style="color:var(--blanco); font-weight:700;">+{i['puntos']}</td>
  <td style="color:var(--gris); font-size:.8rem;">{i['fecha'][:16]}</td>
</tr>''' for i in historial)

        cuerpo = f'''
<div class="grid-3" style="border:1px solid var(--borde); margin-bottom:2rem;">
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{len(historial)}</span>
    <span class="stat-label">Intentos</span>
  </div>
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{correctos}</span>
    <span class="stat-label">Correctos</span>
  </div>
  <div class="stat" style="border:none;">
    <span class="stat-num">{porcentaje}%</span>
    <span class="stat-label">Precision</span>
  </div>
</div>
<table>
  <tr>
    <th>Nivel</th><th>Lenguaje</th><th>Tema</th>
    <th>Resp.</th><th>Estado</th><th>Puntos</th><th>Fecha</th>
  </tr>
  {filas}
</table>'''

    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:2rem; margin-bottom:3rem;">
  <span class="section-label">Actividad</span>
  <div class="linea"></div>
  <h1>Historial</h1>
</div>
{cuerpo}'''
    return base('Historial', contenido, est)


# ── RANKING ────────────────────────────────────────────────────────────────
def pagina_ranking(est, ranking):
    filas = ''
    for i, r in enumerate(ranking):
        pos   = str(i + 1).zfill(2)
        cls   = f'rank-{i+1}' if i < 3 else ''
        tuyo  = r['nombre'] == est['nombre']
        bg    = ' style="background:var(--negro-mid);"' if tuyo else ''
        label = ' &nbsp;<span style="font-size:.6rem; letter-spacing:2px; color:var(--gris);">TU</span>' if tuyo else ''
        filas += f'''
<tr{bg}>
  <td class="{cls}" style="font-size:1.2rem; font-weight:900; letter-spacing:-1px;">{pos}</td>
  <td style="font-weight:700; color:var(--blanco);">{r['nombre']}{label}</td>
  <td style="font-size:1.4rem; font-weight:900; letter-spacing:-1px; color:var(--blanco);">{r['puntos_total']}</td>
  <td style="color:var(--gris);">{r['mejor_racha']}</td>
</tr>'''

    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:2rem; margin-bottom:3rem;">
  <span class="section-label">Competencia</span>
  <div class="linea"></div>
  <h1>Ranking</h1>
</div>
<table>
  <tr>
    <th>#</th><th>Estudiante</th><th>Puntos</th><th>Mejor racha</th>
  </tr>
  {filas}
</table>'''
    return base('Ranking', contenido, est)


# ── RESUMEN ────────────────────────────────────────────────────────────────
def pagina_resumen(est, datos, puntaje):
    total      = datos['total_intentos']
    correctos  = datos['total_correctos']
    porcentaje = int((correctos / total) * 100) if total > 0 else 0
    pt_total   = puntaje['puntos_total'] if puntaje else 0
    mejor      = puntaje['mejor_racha']  if puntaje else 0

    filas = ''
    for l in datos['por_lenguaje']:
        pct = int((l['correctos'] / l['intentos']) * 100) if l['intentos'] > 0 else 0
        filas += f'''
<tr>
  <td style="font-weight:700; color:var(--blanco);">
    {ICONOS.get(l['lenguaje'],'--')} &nbsp; {l['lenguaje']}
  </td>
  <td>{l['intentos']}</td>
  <td>{l['correctos']}</td>
  <td>
    <div style="display:flex; align-items:center; gap:.8rem;">
      <div class="barra-wrap" style="margin:0; width:80px; flex-shrink:0;">
        <div class="barra-fill" style="width:{pct}%;"></div>
      </div>
      <span style="font-size:.8rem; color:var(--blanco-mid);">{pct}%</span>
    </div>
  </td>
  <td style="color:var(--blanco); font-weight:700;">+{l['puntos']}</td>
</tr>'''

    tabla = f'''
<table>
  <tr>
    <th>Lenguaje</th><th>Intentos</th><th>Correctos</th>
    <th>Precision</th><th>Puntos</th>
  </tr>
  {filas}
</table>''' if datos['por_lenguaje'] else '''
<div class="card">
  <p style="color:var(--gris);">Sin datos aun.</p>
  <br>
  <a href="/lenguajes" class="btn-primary">Ir a ejercicios</a>
</div>'''

    contenido = f'''
<div style="border-bottom:1px solid var(--borde); padding-bottom:2rem; margin-bottom:3rem;">
  <span class="section-label">Desempeno</span>
  <div class="linea"></div>
  <h1>Resumen</h1>
</div>

<div class="grid-4" style="border:1px solid var(--borde); margin-bottom:2rem;">
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{total}</span>
    <span class="stat-label">Intentos</span>
  </div>
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{correctos}</span>
    <span class="stat-label">Correctos</span>
  </div>
  <div class="stat" style="border:none; border-right:1px solid var(--borde);">
    <span class="stat-num">{porcentaje}%</span>
    <span class="stat-label">Precision</span>
  </div>
  <div class="stat" style="border:none;">
    <span class="stat-num">{pt_total}</span>
    <span class="stat-label">Puntos totales</span>
  </div>
</div>

{tabla}

<div style="display:flex; gap:1rem; margin-top:2rem;">
  <a href="/lenguajes" class="btn-primary">Seguir practicando</a>
  <a href="/ranking" class="btn-outline">Ver ranking</a>
</div>'''
    return base('Resumen', contenido, est, puntaje)


# ── ERROR ──────────────────────────────────────────────────────────────────
def pagina_error(mensaje, url_volver='/'):
    contenido = f'''
<div style="max-width:500px; margin:4rem auto;">
  <div class="card">
    <span class="section-label">Error</span>
    <div class="linea" style="background:var(--rojo);"></div>
    <h1 style="font-size:2.5rem;">Atencion</h1>
    <p style="margin:1rem 0;">{mensaje}</p>
    <br>
    <a href="{url_volver}" class="btn-primary">Volver</a>
  </div>
</div>'''
    return base('Error', contenido)


# ── 404 ────────────────────────────────────────────────────────────────────
def pagina_404():
    contenido = '''
<div style="max-width:500px; margin:6rem auto; text-align:center;">
  <span style="font-size:8rem; font-weight:900; letter-spacing:-6px;
               color:var(--borde); display:block; line-height:1;">404</span>
  <h1 style="font-size:2rem; margin-bottom:1rem;">No encontrado</h1>
  <p style="margin-bottom:2rem;">La pagina que buscas no existe.</p>
  <a href="/" class="btn-primary">Volver al inicio</a>
</div>'''
    return base('404', contenido)