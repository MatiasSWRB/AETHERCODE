import bd

def validar(id_ej, respuesta_usuario):
    ejercicio = bd.get_ejercicio(id_ej)
    if ejercicio is None:
        return False
    correcta = ejercicio['respuesta_correcta']
    return respuesta_usuario.strip().lower() == correcta.strip().lower()

def get_mensaje(id_ej, correcto):
    ejercicio = bd.get_ejercicio(id_ej)
    if ejercicio is None:
        return "Ejercicio no encontrado."
    if correcto:
        return f"¡Correcto! {ejercicio['explicacion']}"
    else:
        return f"Incorrecto. {ejercicio['explicacion']}"