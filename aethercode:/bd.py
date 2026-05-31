import sqlite3
import hashlib

DB = 'aethercode.db'

def inicializar():
    con = sqlite3.connect(DB)

    con.execute('''
        CREATE TABLE IF NOT EXISTS lenguajes (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    ''')

    con.execute('''
        CREATE TABLE IF NOT EXISTS temas (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre       TEXT NOT NULL,
            id_lenguaje  INTEGER NOT NULL,
            FOREIGN KEY (id_lenguaje) REFERENCES lenguajes(id)
        )
    ''')

    con.execute('''
        CREATE TABLE IF NOT EXISTS ejercicios (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta           TEXT NOT NULL,
            opcion_a           TEXT NOT NULL,
            opcion_b           TEXT NOT NULL,
            opcion_c           TEXT NOT NULL,
            respuesta_correcta TEXT NOT NULL,
            explicacion        TEXT NOT NULL,
            dificultad         TEXT NOT NULL,
            id_tema            INTEGER NOT NULL,
            FOREIGN KEY (id_tema) REFERENCES temas(id)
        )
    ''')

    con.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre           TEXT NOT NULL UNIQUE,
            contrasena       TEXT NOT NULL,
            fecha_registro   TEXT NOT NULL
        )
    ''')

    con.execute('''
        CREATE TABLE IF NOT EXISTS intentos (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            id_estudiante   INTEGER NOT NULL,
            id_ejercicio    INTEGER NOT NULL,
            respuesta       TEXT NOT NULL,
            correcto        INTEGER NOT NULL,
            tiempo_segundos INTEGER NOT NULL,
            puntos          INTEGER NOT NULL,
            fecha           TEXT NOT NULL,
            FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id),
            FOREIGN KEY (id_ejercicio)  REFERENCES ejercicios(id)
        )
    ''')

    con.execute('''
        CREATE TABLE IF NOT EXISTS puntajes (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            id_estudiante  INTEGER NOT NULL UNIQUE,
            puntos_total   INTEGER DEFAULT 0,
            racha_actual   INTEGER DEFAULT 0,
            mejor_racha    INTEGER DEFAULT 0,
            FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)
        )
    ''')

    con.commit()
    con.close()
    print("Base de datos lista.")


# ── Contraseña ────────────────────────────────────────────────
def encriptar(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()


# ── Estudiantes ───────────────────────────────────────────────
def registrar_estudiante(nombre, contrasena):
    try:
        from datetime import datetime
        con = sqlite3.connect(DB)
        con.execute(
            'INSERT INTO estudiantes(nombre, contrasena, fecha_registro) VALUES(?,?,?)',
            (nombre, encriptar(contrasena), datetime.now().isoformat())
        )
        con.execute(
            'INSERT INTO puntajes(id_estudiante) VALUES((SELECT id FROM estudiantes WHERE nombre=?))',
            (nombre,)
        )
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        return False  # nombre ya existe

def login_estudiante(nombre, contrasena):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    fila = con.execute(
        'SELECT * FROM estudiantes WHERE nombre=? AND contrasena=?',
        (nombre, encriptar(contrasena))
    ).fetchone()
    con.close()
    return dict(fila) if fila else None

def get_estudiante(id_est):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    fila = con.execute('SELECT * FROM estudiantes WHERE id=?', (id_est,)).fetchone()
    con.close()
    return dict(fila) if fila else None


# ── Lenguajes y temas ─────────────────────────────────────────
def get_lenguajes():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    filas = con.execute('SELECT * FROM lenguajes').fetchall()
    con.close()
    return [dict(f) for f in filas]

def get_temas(id_lenguaje):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    filas = con.execute(
        'SELECT * FROM temas WHERE id_lenguaje=?', (id_lenguaje,)
    ).fetchall()
    con.close()
    return [dict(f) for f in filas]

def get_lenguaje(id_lenguaje):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    fila = con.execute('SELECT * FROM lenguajes WHERE id=?', (id_lenguaje,)).fetchone()
    con.close()
    return dict(fila) if fila else None

def get_tema(id_tema):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    fila = con.execute('SELECT * FROM temas WHERE id=?', (id_tema,)).fetchone()
    con.close()
    return dict(fila) if fila else None


# ── Ejercicios ────────────────────────────────────────────────
def get_ejercicios(id_tema, dificultad=None):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    if dificultad and dificultad != 'todos':
        filas = con.execute(
            'SELECT * FROM ejercicios WHERE id_tema=? AND dificultad=?',
            (id_tema, dificultad)
        ).fetchall()
    else:
        filas = con.execute(
            'SELECT * FROM ejercicios WHERE id_tema=?', (id_tema,)
        ).fetchall()
    con.close()
    return [dict(f) for f in filas]

def get_ejercicio(id_ej):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    fila = con.execute('SELECT * FROM ejercicios WHERE id=?', (id_ej,)).fetchone()
    con.close()
    return dict(fila) if fila else None

def get_total_ejercicios_tema(id_tema, dificultad=None):
    con = sqlite3.connect(DB)
    if dificultad and dificultad != 'todos':
        total = con.execute(
            'SELECT COUNT(*) FROM ejercicios WHERE id_tema=? AND dificultad=?',
            (id_tema, dificultad)
        ).fetchone()[0]
    else:
        total = con.execute(
            'SELECT COUNT(*) FROM ejercicios WHERE id_tema=?', (id_tema,)
        ).fetchone()[0]
    con.close()
    return total


# ── Intentos y puntaje ────────────────────────────────────────
def calcular_puntos(correcto, tiempo_segundos, racha_actual):
    if not correcto:
        return 0
    puntos = 10
    if tiempo_segundos < 5:
        puntos += 5
    elif tiempo_segundos < 10:
        puntos += 3
    elif tiempo_segundos < 20:
        puntos += 1
    puntos += racha_actual * 2
    return puntos

def guardar_intento(id_estudiante, id_ejercicio, respuesta, correcto, tiempo_segundos):
    from datetime import datetime
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row

    # Leer racha actual
    puntaje = con.execute(
        'SELECT * FROM puntajes WHERE id_estudiante=?', (id_estudiante,)
    ).fetchone()
    racha_actual = puntaje['racha_actual'] if puntaje else 0

    # Calcular puntos
    puntos = calcular_puntos(correcto, tiempo_segundos, racha_actual)

    # Guardar intento
    con.execute(
        'INSERT INTO intentos(id_estudiante,id_ejercicio,respuesta,correcto,tiempo_segundos,puntos,fecha) VALUES(?,?,?,?,?,?,?)',
        (id_estudiante, id_ejercicio, respuesta, int(correcto), tiempo_segundos, puntos, datetime.now().isoformat())
    )

    # Actualizar racha y puntaje total
    nueva_racha = racha_actual + 1 if correcto else 0
    mejor_racha = max(puntaje['mejor_racha'], nueva_racha) if puntaje else nueva_racha
    con.execute('''
        UPDATE puntajes
        SET puntos_total = puntos_total + ?,
            racha_actual = ?,
            mejor_racha  = ?
        WHERE id_estudiante = ?
    ''', (puntos, nueva_racha, mejor_racha, id_estudiante))

    con.commit()
    con.close()
    return puntos

def get_puntaje(id_estudiante):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    fila = con.execute(
        'SELECT * FROM puntajes WHERE id_estudiante=?', (id_estudiante,)
    ).fetchone()
    con.close()
    return dict(fila) if fila else None


# ── Historial ─────────────────────────────────────────────────
def get_historial(id_estudiante, limite=20):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    filas = con.execute('''
        SELECT i.*, e.pregunta, e.dificultad, t.nombre as tema, l.nombre as lenguaje
        FROM intentos i
        JOIN ejercicios e ON i.id_ejercicio = e.id
        JOIN temas t      ON e.id_tema = t.id
        JOIN lenguajes l  ON t.id_lenguaje = l.id
        WHERE i.id_estudiante = ?
        ORDER BY i.id DESC LIMIT ?
    ''', (id_estudiante, limite)).fetchall()
    con.close()
    return [dict(f) for f in filas]


# ── Ranking ───────────────────────────────────────────────────
def get_ranking(limite=10):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    filas = con.execute('''
        SELECT e.nombre, p.puntos_total, p.mejor_racha
        FROM puntajes p
        JOIN estudiantes e ON p.id_estudiante = e.id
        ORDER BY p.puntos_total DESC
        LIMIT ?
    ''', (limite,)).fetchall()
    con.close()
    return [dict(f) for f in filas]


# ── Resumen ───────────────────────────────────────────────────
def get_resumen(id_estudiante):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    total_intentos  = con.execute(
        'SELECT COUNT(*) FROM intentos WHERE id_estudiante=?', (id_estudiante,)
    ).fetchone()[0]
    total_correctos = con.execute(
        'SELECT COUNT(*) FROM intentos WHERE id_estudiante=? AND correcto=1', (id_estudiante,)
    ).fetchone()[0]
    por_lenguaje = con.execute('''
        SELECT l.nombre as lenguaje,
               COUNT(*) as intentos,
               SUM(i.correcto) as correctos,
               SUM(i.puntos) as puntos
        FROM intentos i
        JOIN ejercicios e ON i.id_ejercicio = e.id
        JOIN temas t      ON e.id_tema = t.id
        JOIN lenguajes l  ON t.id_lenguaje = l.id
        WHERE i.id_estudiante = ?
        GROUP BY l.nombre
    ''', (id_estudiante,)).fetchall()
    con.close()
    return {
        'total_intentos':  total_intentos,
        'total_correctos': total_correctos,
        'por_lenguaje':    [dict(f) for f in por_lenguaje]
    }


# ── Test ──────────────────────────────────────────────────────
if __name__ == '__main__':
    inicializar()
    print("Tablas creadas correctamente.")
    print("Lenguajes:", get_lenguajes())