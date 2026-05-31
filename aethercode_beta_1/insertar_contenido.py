import sqlite3
import bd

bd.inicializar()
con = sqlite3.connect(bd.DB)

# ── Limpiar todo ──────────────────────────────────────────────
con.execute('DELETE FROM ejercicios')
con.execute('DELETE FROM temas')
con.execute('DELETE FROM lenguajes')
con.execute("DELETE FROM sqlite_sequence WHERE name IN ('ejercicios','temas','lenguajes')")
con.commit()

# ── Lenguajes ─────────────────────────────────────────────────
lenguajes = ['Python', 'JavaScript', 'Java', 'C++', 'SQL']
for l in lenguajes:
    con.execute('INSERT INTO lenguajes(nombre) VALUES(?)', (l,))
con.commit()
print("Lenguajes insertados.")

# ── Temas (5 por lenguaje) ────────────────────────────────────
temas = [
    # Python (id_lenguaje=1)
    ('Variables y tipos de datos', 1),
    ('Condicionales',              1),
    ('Bucles',                     1),
    ('Funciones',                  1),
    ('Estructuras de datos',       1),
    # JavaScript (id_lenguaje=2)
    ('Variables y tipos de datos', 2),
    ('Condicionales',              2),
    ('Bucles',                     2),
    ('Funciones',                  2),
    ('Estructuras de datos',       2),
    # Java (id_lenguaje=3)
    ('Variables y tipos de datos', 3),
    ('Condicionales',              3),
    ('Bucles',                     3),
    ('Funciones',                  3),
    ('Estructuras de datos',       3),
    # C++ (id_lenguaje=4)
    ('Variables y tipos de datos', 4),
    ('Condicionales',              4),
    ('Bucles',                     4),
    ('Funciones',                  4),
    ('Estructuras de datos',       4),
    # SQL (id_lenguaje=5)
    ('Consultas básicas',          5),
    ('Filtros y condiciones',      5),
    ('Joins',                      5),
    ('Funciones de agregación',    5),
    ('Subconsultas',               5),
]
for t in temas:
    con.execute('INSERT INTO temas(nombre, id_lenguaje) VALUES(?,?)', t)
con.commit()
print("Temas insertados.")

# ── Ejercicios ────────────────────────────────────────────────
# Formato: (pregunta, op_a, op_b, op_c, correcta, explicacion, dificultad, id_tema)

ejercicios = [

    # ══ PYTHON — Variables y tipos de datos (id_tema=1) ══════
    ('¿Cuál es el tipo de dato de x = 5?',
     'a) str', 'b) int', 'c) float',
     'b', 'En Python, un número entero sin punto decimal es de tipo int.',
     'facil', 1),

    ('¿Qué imprime print(type("hola"))?',
     'a) str', 'b) <class str>', 'c) <class \'str\'>',
     'c', 'type() devuelve el tipo con el formato <class \'tipo\'>.',
     'facil', 1),

    ('¿Cuál de estas es una variable válida en Python?',
     'a) 2nombre', 'b) nombre_2', 'c) nombre-2',
     'b', 'Las variables no pueden empezar con número ni contener guiones.',
     'facil', 1),

    ('¿Qué resultado da print(10 / 3)?',
     'a) 3', 'b) 3.33', 'c) 3.3333333333333335',
     'c', 'La división / en Python siempre devuelve float con todos sus decimales.',
     'medio', 1),

    ('¿Qué hace el operador // en Python?',
     'a) División normal', 'b) División entera', 'c) Módulo',
     'b', '// es división entera: descarta los decimales. 10//3 = 3.',
     'medio', 1),

    ('¿Qué devuelve bool(0)?',
     'a) True', 'b) False', 'c) Error',
     'b', 'En Python, 0 se evalúa como False. Cualquier otro número es True.',
     'medio', 1),

    ('¿Qué imprime print(10 % 3)?',
     'a) 3', 'b) 1', 'c) 0',
     'b', '% es el operador módulo. 10 dividido 3 da 3 con residuo 1.',
     'facil', 1),

    ('¿Qué tipo devuelve 5 == 5?',
     'a) int', 'b) str', 'c) bool',
     'c', 'Las comparaciones siempre devuelven bool: True o False.',
     'medio', 1),

    ('¿Cuál es la forma correcta de convertir "5" a entero?',
     'a) int["5"]', 'b) int("5")', 'c) to_int("5")',
     'b', 'La función int() convierte un string numérico a entero.',
     'facil', 1),

    ('¿Qué imprime print(2 ** 8)?',
     'a) 16', 'b) 256', 'c) 64',
     'b', '** es el operador de potencia. 2 elevado a 8 es 256.',
     'dificil', 1),

    # ══ PYTHON — Condicionales (id_tema=2) ═══════════════════
    ('¿Qué imprime este código?\nx = 10\nif x > 5:\n    print("mayor")',
     'a) menor', 'b) nada', 'c) mayor',
     'c', 'x vale 10, que sí es mayor que 5, entonces entra al if.',
     'facil', 2),

    ('¿Cuál es la palabra clave para condición alternativa en Python?',
     'a) else if', 'b) elif', 'c) elseif',
     'b', 'Python usa elif (contracción de else if) para condiciones encadenadas.',
     'facil', 2),

    ('¿Qué imprime?\nx = 3\nif x > 5:\n    print("A")\nelse:\n    print("B")',
     'a) A', 'b) B', 'c) nada',
     'b', 'x=3 no es mayor que 5, entonces va al else e imprime B.',
     'facil', 2),

    ('¿Qué operador se usa para comparar igualdad en Python?',
     'a) =', 'b) ===', 'c) ==',
     'c', '= asigna valor. == compara si dos valores son iguales.',
     'facil', 2),

    ('¿Qué imprime?\nx = 15\nif x < 10:\n    print("A")\nelif x < 20:\n    print("B")\nelse:\n    print("C")',
     'a) A', 'b) B', 'c) C',
     'b', 'x=15 no es menor que 10, pero sí menor que 20, entonces imprime B.',
     'medio', 2),

    ('¿Cuál es el resultado de: 5 > 3 and 2 < 1?',
     'a) True', 'b) False', 'c) Error',
     'b', 'and requiere que ambas condiciones sean True. 2 < 1 es False.',
     'medio', 2),

    ('¿Cuál es el resultado de: 5 > 3 or 2 < 1?',
     'a) True', 'b) False', 'c) Error',
     'a', 'or solo necesita que una condición sea True. 5 > 3 es True.',
     'medio', 2),

    ('¿Qué hace not True?',
     'a) True', 'b) False', 'c) Error',
     'b', 'not invierte el valor booleano. not True = False.',
     'facil', 2),

    ('¿Qué imprime?\nx = 5\nprint("par") if x % 2 == 0 else print("impar")',
     'a) par', 'b) impar', 'c) Error',
     'b', 'Es un if ternario. x=5 es impar porque 5 % 2 = 1, no 0.',
     'dificil', 2),

    ('¿Qué operador verifica que dos valores NO sean iguales?',
     'a) !', 'b) <>',  'c) !=',
     'c', 'En Python, != es el operador de desigualdad.',
     'facil', 2),

    # ══ PYTHON — Bucles (id_tema=3) ══════════════════════════
    ('¿Cuántas veces itera for i in range(4)?',
     'a) 3', 'b) 5', 'c) 4',
     'c', 'range(4) genera 0,1,2,3 — exactamente 4 valores.',
     'facil', 3),

    ('¿Qué imprime for i in range(2, 5): print(i)?',
     'a) 2 3 4', 'b) 2 3 4 5', 'c) 1 2 3 4',
     'a', 'range(2,5) genera desde 2 hasta 4 (el límite superior es exclusivo).',
     'facil', 3),

    ('¿Qué hace break dentro de un bucle?',
     'a) Pausa el bucle', 'b) Sale del bucle', 'c) Continúa al siguiente',
     'b', 'break termina el bucle inmediatamente.',
     'facil', 3),

    ('¿Qué hace continue dentro de un bucle?',
     'a) Sale del bucle', 'b) Pausa el bucle', 'c) Salta a la siguiente iteración',
     'c', 'continue omite el resto del cuerpo y va a la siguiente vuelta.',
     'medio', 3),

    ('¿Cuántas veces imprime este while?\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1',
     'a) 2', 'b) 3', 'c) 4',
     'b', 'x toma valores 0, 1, 2. Cuando x=3 la condición es False y para.',
     'medio', 3),

    ('¿Qué imprime range(0, 10, 2)?',
     'a) 0 2 4 6 8', 'b) 0 2 4 6 8 10', 'c) 2 4 6 8',
     'a', 'El tercer parámetro es el paso. range(0,10,2) genera 0,2,4,6,8.',
     'medio', 3),

    ('¿Qué tipo de bucle usarías cuando no sabes cuántas veces repetir?',
     'a) for', 'b) while', 'c) loop',
     'b', 'while repite mientras una condición sea True, sin número fijo de vueltas.',
     'facil', 3),

    ('¿Qué imprime?\nfor i in range(3):\n    if i == 1:\n        break\n    print(i)',
     'a) 0 1 2', 'b) 0', 'c) 1 2',
     'b', 'Imprime 0, luego cuando i=1 el break sale del bucle.',
     'dificil', 3),

    ('¿Cuál es el resultado?\ntotal = 0\nfor i in range(1, 4):\n    total += i\nprint(total)',
     'a) 3', 'b) 6', 'c) 4',
     'b', 'total acumula 1+2+3 = 6.',
     'medio', 3),

    ('¿Qué hace for i in range(5, 0, -1)?',
     'a) Error', 'b) Cuenta de 1 a 5', 'c) Cuenta de 5 a 1',
     'c', 'El paso -1 hace que el rango vaya hacia atrás: 5,4,3,2,1.',
     'dificil', 3),

    # ══ PYTHON — Funciones (id_tema=4) ═══════════════════════
    ('¿Cuál es la palabra clave para definir una función en Python?',
     'a) function', 'b) def', 'c) func',
     'b', 'En Python las funciones se definen con def nombre():.',
     'facil', 4),

    ('¿Qué devuelve una función sin return?',
     'a) 0', 'b) None', 'c) Error',
     'b', 'Si no hay return, Python devuelve None automáticamente.',
     'medio', 4),

    ('¿Qué imprime?\ndef doble(x):\n    return x * 2\nprint(doble(4))',
     'a) 4', 'b) 42', 'c) 8',
     'c', 'doble(4) calcula 4 * 2 = 8.',
     'facil', 4),

    ('¿Qué son los parámetros por defecto?',
     'a) Parámetros obligatorios', 'b) Parámetros con valor predefinido', 'c) Parámetros vacíos',
     'b', 'def saludo(nombre="mundo"): usa "mundo" si no se pasa ningún valor.',
     'medio', 4),

    ('¿Qué imprime?\ndef suma(a, b=10):\n    return a + b\nprint(suma(5))',
     'a) 5', 'b) 10', 'c) 15',
     'c', 'b tiene valor por defecto 10. suma(5) calcula 5 + 10 = 15.',
     'medio', 4),

    ('¿Qué hace *args en una función?',
     'a) Un solo argumento', 'b) Argumentos con nombre', 'c) Múltiples argumentos posicionales',
     'c', '*args permite pasar cualquier cantidad de argumentos a la función.',
     'dificil', 4),

    ('¿Pueden las funciones en Python devolver múltiples valores?',
     'a) No', 'b) Solo con listas', 'c) Sí, con return a, b',
     'c', 'return a, b devuelve una tupla con ambos valores.',
     'dificil', 4),

    ('¿Qué es una función lambda?',
     'a) Una función sin nombre', 'b) Una función recursiva', 'c) Una función de módulo',
     'a', 'lambda es una función anónima de una sola expresión: lambda x: x*2.',
     'dificil', 4),

    ('¿Qué imprime?\ndef conta():\n    x = 5\nprint(x)',
     'a) 5', 'b) None', 'c) Error',
     'c', 'x está definida dentro de la función y no es accesible fuera (scope local).',
     'dificil', 4),

    ('¿Cuántas veces se llama a si misma?\ndef cuenta(n):\n    if n == 0:\n        return\n    cuenta(n-1)\ncuenta(3)',
     'a) 3', 'b) 4', 'c) 2',
     'a', 'cuenta(3) llama a cuenta(2), que llama a cuenta(1), que llama a cuenta(0). 3 veces.',
     'dificil', 4),

    # ══ PYTHON — Estructuras de datos (id_tema=5) ═════════════
    ('¿Cuál es la forma correcta de crear una lista en Python?',
     'a) lista = (1,2,3)', 'b) lista = [1,2,3]', 'c) lista = {1,2,3}',
     'b', 'Las listas se crean con corchetes []. Los paréntesis son tuplas y las llaves son sets.',
     'facil', 5),

    ('¿Qué devuelve len([1, 2, 3, 4])?',
     'a) 3', 'b) 4', 'c) 5',
     'b', 'len() devuelve la cantidad de elementos. La lista tiene 4 elementos.',
     'facil', 5),

    ('¿Cómo se accede al primer elemento de lista = [10, 20, 30]?',
     'a) lista[1]', 'b) lista[0]', 'c) lista.first()',
     'b', 'Los índices en Python empiezan en 0. lista[0] es el primer elemento.',
     'facil', 5),

    ('¿Qué hace lista.append(5)?',
     'a) Inserta 5 al inicio', 'b) Agrega 5 al final', 'c) Elimina el 5',
     'b', 'append() agrega un elemento al final de la lista.',
     'facil', 5),

    ('¿Cuál es la diferencia entre lista y tupla?',
     'a) No hay diferencia', 'b) La tupla es mutable', 'c) La lista es mutable, la tupla no',
     'c', 'Las listas se pueden modificar. Las tuplas son inmutables una vez creadas.',
     'medio', 5),

    ('¿Qué imprime [1,2,3,4,5][1:3]?',
     'a) [1,2,3]', 'b) [2,3]', 'c) [2,3,4]',
     'b', 'El slicing [1:3] toma desde índice 1 hasta 2 (el 3 es exclusivo).',
     'medio', 5),

    ('¿Cómo se crea un diccionario en Python?',
     'a) d = [clave:valor]', 'b) d = (clave:valor)', 'c) d = {"clave": valor}',
     'c', 'Los diccionarios usan llaves {} con pares clave:valor.',
     'facil', 5),

    ('¿Qué devuelve {"a":1,"b":2}.keys()?',
     'a) [1, 2]', 'b) ["a", "b"]', 'c) dict_keys(["a","b"])',
     'c', '.keys() devuelve un objeto dict_keys con las claves del diccionario.',
     'medio', 5),

    ('¿Qué estructura NO permite duplicados?',
     'a) lista', 'b) set', 'c) tupla',
     'b', 'Un set es una colección sin duplicados y sin orden.',
     'medio', 5),

    ('¿Qué imprime?\nd = {"x": 10}\nd["y"] = 20\nprint(len(d))',
     'a) 1', 'b) 3', 'c) 2',
     'c', 'El diccionario empieza con 1 clave y se agrega otra. len(d) = 2.',
     'dificil', 5),

    # ══ JAVASCRIPT — Variables y tipos de datos (id_tema=6) ═══
    ('¿Cuál es la forma moderna de declarar una variable en JS?',
     'a) var x = 5', 'b) let x = 5', 'c) variable x = 5',
     'b', 'let es la forma moderna. var tiene problemas de scope. const es para valores fijos.',
     'facil', 6),

    ('¿Qué imprime typeof "hola"?',
     'a) string', 'b) str', 'c) text',
     'a', 'En JavaScript los tipos se llaman string, number, boolean, etc.',
     'facil', 6),

    ('¿Cuál es la diferencia entre == y === en JS?',
     'a) No hay diferencia', 'b) === compara valor y tipo', 'c) == compara tipo',
     'b', '== convierte tipos antes de comparar. === compara valor Y tipo sin conversión.',
     'medio', 6),

    ('¿Qué devuelve typeof null?',
     'a) null', 'b) undefined', 'c) object',
     'c', 'Es un bug histórico de JS. typeof null devuelve "object" aunque null no es un objeto.',
     'dificil', 6),

    ('¿Cómo se declara una constante en JavaScript?',
     'a) const x = 5', 'b) let x = 5', 'c) fixed x = 5',
     'a', 'const declara una variable cuyo valor no puede reasignarse.',
     'facil', 6),

    ('¿Qué imprime console.log(5 + "3")?',
     'a) 8', 'b) 53', 'c) Error',
     'b', 'JS convierte el 5 a string y concatena: "5" + "3" = "53".',
     'medio', 6),

    ('¿Qué valor tiene una variable declarada pero no inicializada?',
     'a) null', 'b) 0', 'c) undefined',
     'c', 'En JS, una variable declarada sin valor tiene el valor undefined.',
     'medio', 6),

    ('¿Qué imprime console.log(Boolean(0))?',
     'a) true', 'b) false', 'c) 0',
     'b', '0 es un valor falsy en JavaScript. Boolean(0) devuelve false.',
     'medio', 6),

    ('¿Cuál de estos es un valor falsy en JS?',
     'a) "false"', 'b) []', 'c) ""',
     'c', 'Un string vacío "" es falsy. "false" es truthy porque es un string no vacío.',
     'dificil', 6),

    ('¿Qué hace el operador ?? en JS?',
     'a) Comparación estricta', 'b) Devuelve el lado derecho si el izquierdo es null o undefined', 'c) Negación doble',
     'b', '?? es el operador nullish coalescing. x ?? "default" devuelve "default" solo si x es null o undefined.',
     'dificil', 6),

    # ══ JAVASCRIPT — Condicionales (id_tema=7) ════════════════
    ('¿Cómo se escribe un if en JavaScript?',
     'a) if x > 5 {', 'b) if (x > 5) {', 'c) if [x > 5] {',
     'b', 'En JS la condición va entre paréntesis y el bloque entre llaves.',
     'facil', 7),

    ('¿Qué es el operador ternario en JS?',
     'a) if/else/elif', 'b) condición ? valorTrue : valorFalse', 'c) switch/case',
     'b', 'El ternario es una forma corta del if/else en una sola línea.',
     'medio', 7),

    ('¿Qué imprime?\nlet x = 10;\nif (x > 5) { console.log("A"); } else { console.log("B"); }',
     'a) A', 'b) B', 'c) AB',
     'a', 'x=10 es mayor que 5, entra al if e imprime A.',
     'facil', 7),

    ('¿Para qué sirve switch en JS?',
     'a) Para bucles', 'b) Para comparar un valor contra múltiples casos', 'c) Para funciones',
     'b', 'switch evalúa una expresión y ejecuta el case que coincida.',
     'medio', 7),

    ('¿Qué pasa si omites break en un case de switch?',
     'a) Error', 'b) Ejecuta solo ese case', 'c) Ejecuta ese case y los siguientes',
     'c', 'Sin break ocurre fall-through: sigue ejecutando los cases siguientes.',
     'dificil', 7),

    ('¿Cuál es el resultado de: true && false?',
     'a) true', 'b) false', 'c) undefined',
     'b', '&& requiere que ambos sean true. false hace que el resultado sea false.',
     'facil', 7),

    ('¿Cuál es el resultado de: false || true?',
     'a) false', 'b) true', 'c) undefined',
     'b', '|| solo necesita que uno sea true. true hace que el resultado sea true.',
     'facil', 7),

    ('¿Qué devuelve !true?',
     'a) true', 'b) false', 'c) undefined',
     'b', '! es el operador NOT. Invierte el valor booleano.',
     'facil', 7),

    ('¿Qué imprime?\nlet x = 5;\nconsole.log(x > 3 ? "mayor" : "menor");',
     'a) mayor', 'b) menor', 'c) Error',
     'a', 'x=5 es mayor que 3, la condición es true, imprime "mayor".',
     'medio', 7),

    ('¿Cuál es el resultado de: null == undefined?',
     'a) false', 'b) Error', 'c) true',
     'c', 'Con ==, null y undefined son iguales entre sí pero no con otros valores.',
     'dificil', 7),

    # ══ JAVASCRIPT — Bucles (id_tema=8) ══════════════════════
    ('¿Cómo se escribe un for básico en JS?',
     'a) for i in range(5):', 'b) for (let i=0; i<5; i++)', 'c) for i = 0 to 5',
     'b', 'El for en JS tiene tres partes: inicialización; condición; incremento.',
     'facil', 8),

    ('¿Qué hace i++ en JS?',
     'a) Decrementa i en 1', 'b) Incrementa i en 1', 'c) Multiplica i por 2',
     'b', '++ es el operador de incremento. i++ es equivalente a i = i + 1.',
     'facil', 8),

    ('¿Para qué sirve forEach en un array?',
     'a) Filtrar elementos', 'b) Ejecutar una función por cada elemento', 'c) Ordenar el array',
     'b', 'forEach recorre cada elemento y ejecuta una función callback.',
     'medio', 8),

    ('¿Qué devuelve [1,2,3].map(x => x * 2)?',
     'a) [1,2,3]', 'b) 12', 'c) [2,4,6]',
     'c', 'map crea un nuevo array aplicando la función a cada elemento.',
     'medio', 8),

    ('¿Cuál es la diferencia entre for...in y for...of?',
     'a) No hay diferencia', 'b) for...in itera claves, for...of itera valores', 'c) for...of itera claves',
     'b', 'for...in itera las claves de un objeto. for...of itera los valores de un iterable.',
     'dificil', 8),

    ('¿Qué devuelve [1,2,3,4].filter(x => x > 2)?',
     'a) [3,4]', 'b) [1,2]', 'c) [2,3,4]',
     'a', 'filter devuelve un nuevo array solo con los elementos que cumplen la condición.',
     'medio', 8),

    ('¿Qué hace while (true) {}?',
     'a) No ejecuta nada', 'b) Bucle infinito', 'c) Error',
     'b', 'La condición siempre es true, por lo que el bucle nunca termina.',
     'facil', 8),

    ('¿Qué devuelve [1,2,3].reduce((acc, x) => acc + x, 0)?',
     'a) 3', 'b) 123', 'c) 6',
     'c', 'reduce acumula: empieza en 0, suma 1→1, suma 2→3, suma 3→6.',
     'dificil', 8),

    ('¿Qué imprime?\nfor (let i = 0; i < 3; i++) { if (i===1) continue; console.log(i); }',
     'a) 0 1 2', 'b) 0 2', 'c) 1',
     'b', 'continue salta la iteración cuando i=1. Imprime 0 y 2.',
     'dificil', 8),

    ('¿Cuántas veces ejecuta este bucle?\nlet i = 5;\nwhile (i > 0) { i -= 2; }',
     'a) 2', 'b) 5', 'c) 3',
     'c', 'i va: 5→3→1→-1. La condición falla cuando i=-1. Ejecuta 3 veces.',
     'dificil', 8),

    # ══ JAVASCRIPT — Funciones (id_tema=9) ═══════════════════
    ('¿Cómo se declara una función en JS?',
     'a) def miFuncion() {}', 'b) function miFuncion() {}', 'c) func miFuncion() {}',
     'b', 'En JavaScript las funciones se declaran con la palabra clave function.',
     'facil', 9),

    ('¿Qué es una arrow function?',
     'a) Una función con nombre', 'b) Una función con sintaxis corta: () => {}', 'c) Una función recursiva',
     'b', 'Las arrow functions son una sintaxis compacta: const doble = x => x * 2.',
     'medio', 9),

    ('¿Qué devuelve esta función?\nconst suma = (a, b) => a + b;\nconsole.log(suma(3, 4));',
     'a) 34', 'b) 7', 'c) undefined',
     'b', 'La arrow function retorna implícitamente a + b. 3 + 4 = 7.',
     'facil', 9),

    ('¿Qué es el hoisting en funciones?',
     'a) Que las funciones se borran al usarlas', 'b) Que las funciones declaradas se pueden usar antes de definirlas', 'c) Que las funciones son privadas',
     'b', 'JS mueve las declaraciones de funciones al inicio del scope antes de ejecutar.',
     'dificil', 9),

    ('¿Qué es un callback?',
     'a) Una función que llama a otra', 'b) Una función que se pasa como argumento', 'c) Una función recursiva',
     'b', 'Un callback es una función que se pasa como parámetro y se ejecuta después.',
     'medio', 9),

    ('¿Qué imprime?\nfunction saludo(nombre = "mundo") { return "Hola " + nombre; }\nconsole.log(saludo());',
     'a) Hola', 'b) Hola undefined', 'c) Hola mundo',
     'c', 'nombre tiene valor por defecto "mundo". saludo() usa ese valor.',
     'medio', 9),

    ('¿Qué hace el operador ... (spread) en funciones?',
     'a) Multiplica argumentos', 'b) Expande un array como argumentos individuales', 'c) Crea una copia',
     'b', 'Math.max(...[1,2,3]) es equivalente a Math.max(1,2,3).',
     'dificil', 9),

    ('¿Qué es una función pura?',
     'a) Una función sin parámetros', 'b) Una función que siempre devuelve el mismo resultado para los mismos argumentos', 'c) Una función sin return',
     'b', 'Una función pura no tiene efectos secundarios y es determinista.',
     'dificil', 9),

    ('¿Qué devuelve una función sin return en JS?',
     'a) 0', 'b) null', 'c) undefined',
     'c', 'En JS, una función sin return devuelve undefined.',
     'medio', 9),

    ('¿Qué es una IIFE?',
     'a) Una función que se llama a sí misma', 'b) Una función que se ejecuta inmediatamente al definirse', 'c) Una función infinita',
     'b', 'IIFE: Immediately Invoked Function Expression. Se define y ejecuta al mismo tiempo: (function(){})().',
     'dificil', 9),

    # ══ JAVASCRIPT — Estructuras de datos (id_tema=10) ════════
    ('¿Cómo se crea un array en JS?',
     'a) let a = (1,2,3)', 'b) let a = [1,2,3]', 'c) let a = {1,2,3}',
     'b', 'Los arrays en JS se crean con corchetes [].',
     'facil', 10),

    ('¿Qué hace push() en un array?',
     'a) Elimina el último elemento', 'b) Agrega un elemento al final', 'c) Agrega al inicio',
     'b', 'push() agrega uno o más elementos al final del array.',
     'facil', 10),

    ('¿Qué hace pop() en un array?',
     'a) Elimina y devuelve el último elemento', 'b) Agrega al final', 'c) Ordena el array',
     'a', 'pop() elimina el último elemento y lo devuelve.',
     'facil', 10),

    ('¿Cómo se crea un objeto en JS?',
     'a) let o = [nombre:"Ana"]', 'b) let o = {nombre: "Ana"}', 'c) let o = (nombre="Ana")',
     'b', 'Los objetos en JS usan llaves {} con pares clave: valor.',
     'facil', 10),

    ('¿Qué devuelve Object.keys({a:1, b:2})?',
     'a) [1, 2]', 'b) ["a","b"]', 'c) {a,b}',
     'b', 'Object.keys() devuelve un array con las claves del objeto.',
     'medio', 10),

    ('¿Qué es un Map en JS?',
     'a) Un array especial', 'b) Una función de transformación', 'c) Una colección de pares clave-valor que acepta cualquier tipo de clave',
     'c', 'Map es como un objeto pero acepta cualquier tipo como clave, no solo strings.',
     'dificil', 10),

    ('¿Qué es un Set en JS?',
     'a) Una colección sin duplicados', 'b) Un objeto ordenado', 'c) Un array especial con índices',
     'a', 'Set almacena valores únicos. Si agregas un duplicado, lo ignora.',
     'medio', 10),

    ('¿Qué devuelve [1,2,3].indexOf(2)?',
     'a) 2', 'b) 1', 'c) true',
     'b', 'indexOf devuelve el índice del elemento. El 2 está en la posición 1.',
     'medio', 10),

    ('¿Qué hace splice(1, 2) en un array?',
     'a) Devuelve desde el índice 1', 'b) Elimina 2 elementos desde el índice 1', 'c) Agrega 2 elementos',
     'b', 'splice(inicio, cantidad) elimina elementos del array modificándolo.',
     'dificil', 10),

    ('¿Qué devuelve [1,2,3].includes(4)?',
     'a) 4', 'b) true', 'c) false',
     'c', 'includes() devuelve true si el elemento existe, false si no. El 4 no está.',
     'facil', 10),

    # ══ JAVA — Variables y tipos de datos (id_tema=11) ════════
    ('¿Cómo se declara un entero en Java?',
     'a) int x = 5;', 'b) x = 5;', 'c) integer x = 5;',
     'a', 'Java es tipado estático: debes declarar el tipo antes del nombre.',
     'facil', 11),

    ('¿Cuál es el tipo para texto en Java?',
     'a) str', 'b) text', 'c) String',
     'c', 'En Java, String (con S mayúscula) es la clase para texto.',
     'facil', 11),

    ('¿Qué es una variable final en Java?',
     'a) La última variable del programa', 'b) Una constante que no puede cambiar', 'c) Una variable global',
     'b', 'final es el equivalente de const en Java. El valor no puede reasignarse.',
     'medio', 11),

    ('¿Cuánto ocupa un int en Java?',
     'a) 8 bits', 'b) 16 bits', 'c) 32 bits',
     'c', 'int en Java ocupa 32 bits. Para 64 bits se usa long.',
     'dificil', 11),

    ('¿Cuál es la diferencia entre int e Integer en Java?',
     'a) No hay diferencia', 'b) int es primitivo, Integer es objeto', 'c) Integer es más pequeño',
     'b', 'int es un tipo primitivo. Integer es su clase wrapper que permite usar métodos.',
     'dificil', 11),

    ('¿Cómo se imprime en Java?',
     'a) print("hola")', 'b) console.log("hola")', 'c) System.out.println("hola");',
     'c', 'En Java se usa System.out.println() para imprimir con salto de línea.',
     'facil', 11),

    ('¿Qué tipo usar para números decimales en Java?',
     'a) decimal', 'b) double', 'c) float64',
     'b', 'double es el tipo de punto flotante de 64 bits más usado en Java.',
     'facil', 11),

    ('¿Qué hace el casting (int) 3.9 en Java?',
     'a) Redondea a 4', 'b) Trunca a 3', 'c) Error',
     'b', 'El casting trunca (no redondea). (int) 3.9 = 3.',
     'medio', 11),

    ('¿Cuál es el tipo booleano en Java?',
     'a) Boolean', 'b) bool', 'c) boolean',
     'c', 'En Java el tipo primitivo es boolean (minúscula). Boolean es la clase wrapper.',
     'medio', 11),

    ('¿Qué imprime System.out.println("Hola" + 5 + 3)?',
     'a) Hola8', 'b) Hola53', 'c) Error',
     'b', 'Java concatena de izquierda a derecha. "Hola"+5 = "Hola5", luego +"3" = "Hola53".',
     'dificil', 11),

    # ══ JAVA — Condicionales (id_tema=12) ═════════════════════
    ('¿Cómo se escribe un if en Java?',
     'a) if x > 5 {', 'b) if (x > 5) {', 'c) if [x > 5] {',
     'b', 'En Java la condición va entre paréntesis y el bloque entre llaves.',
     'facil', 12),

    ('¿Qué operador se usa para AND en Java?',
     'a) and', 'b) &', 'c) &&',
     'c', '&& es el operador AND lógico en Java. & también existe pero evalúa ambos lados.',
     'medio', 12),

    ('¿Qué operador se usa para OR en Java?',
     'a) or', 'b) ||', 'c) |',
     'b', '|| es el operador OR lógico en Java.',
     'facil', 12),

    ('¿Qué es el operador ternario en Java?',
     'a) if/else/elif', 'b) condición ? valorTrue : valorFalse', 'c) switch',
     'b', 'El ternario funciona igual que en JS: condición ? siTrue : siFalse.',
     'medio', 12),

    ('¿Qué imprime?\nint x = 7;\nif (x > 10) { System.out.println("A"); } else { System.out.println("B"); }',
     'a) A', 'b) B', 'c) AB',
     'b', 'x=7 no es mayor que 10, entra al else e imprime B.',
     'facil', 12),

    ('¿Qué diferencia hay entre == y .equals() en Java para Strings?',
     'a) No hay diferencia', 'b) == compara referencias, .equals() compara contenido', 'c) .equals() es más lento',
     'b', 'Para comparar el contenido de Strings en Java siempre usa .equals().',
     'dificil', 12),

    ('¿Qué hace instanceof en Java?',
     'a) Crea una instancia', 'b) Verifica si un objeto es de cierta clase', 'c) Compara valores',
     'b', 'instanceof devuelve true si el objeto es una instancia de esa clase.',
     'dificil', 12),

    ('¿Cuándo se usa switch en Java?',
     'a) Para bucles', 'b) Para comparar una variable contra múltiples valores', 'c) Para funciones',
     'b', 'switch evalúa una expresión y ejecuta el bloque del case que coincida.',
     'medio', 12),

    ('¿Qué pasa si no hay break en un case de switch en Java?',
     'a) Error de compilación', 'b) Solo ejecuta ese case', 'c) Ejecuta ese y los siguientes casos',
     'c', 'Sin break ocurre fall-through en Java igual que en JS.',
     'dificil', 12),

    ('¿Qué imprime?\nint x = 5;\nString r = (x > 3) ? "mayor" : "menor";\nSystem.out.println(r);',
     'a) mayor', 'b) menor', 'c) Error',
     'a', 'x=5 es mayor que 3, el ternario devuelve "mayor".',
     'medio', 12),

    # ══ JAVA — Bucles (id_tema=13) ════════════════════════════
    ('¿Cómo se escribe un for básico en Java?',
     'a) for i in range(5):', 'b) for (int i=0; i<5; i++)', 'c) for i = 0 to 5',
     'b', 'El for en Java tiene: inicialización; condición; incremento.',
     'facil', 13),

    ('¿Qué hace i-- en Java?',
     'a) Incrementa i', 'b) Decrementa i en 1', 'c) Divide i entre 2',
     'b', '-- es el operador de decremento. i-- es equivalente a i = i - 1.',
     'facil', 13),

    ('¿Cómo se itera sobre un array en Java con for-each?',
     'a) for (int x : array)', 'b) for (x in array)', 'c) foreach (array as x)',
     'a', 'El for-each en Java usa los dos puntos : para separar variable y colección.',
     'medio', 13),

    ('¿Qué hace break en un bucle Java?',
     'a) Pausa el bucle', 'b) Sale del bucle', 'c) Continúa al siguiente',
     'b', 'break termina el bucle inmediatamente.',
     'facil', 13),

    ('¿Cuántas veces ejecuta?\nfor (int i = 0; i < 5; i += 2)',
     'a) 5', 'b) 2', 'c) 3',
     'c', 'i toma valores 0, 2, 4. Cuando i=6 la condición falla. 3 iteraciones.',
     'medio', 13),

    ('¿Qué hace continue en Java?',
     'a) Sale del bucle', 'b) Salta a la siguiente iteración', 'c) Pausa la ejecución',
     'b', 'continue omite el resto del cuerpo y va a la siguiente vuelta del bucle.',
     'medio', 13),

    ('¿Cuál es la diferencia entre while y do-while en Java?',
     'a) No hay diferencia', 'b) do-while ejecuta al menos una vez', 'c) while ejecuta siempre',
     'b', 'do-while ejecuta el cuerpo primero y luego evalúa la condición.',
     'medio', 13),

    ('¿Qué imprime?\nint s = 0;\nfor (int i = 1; i <= 4; i++) s += i;\nSystem.out.println(s);',
     'a) 4', 'b) 10', 'c) 6',
     'b', 's acumula 1+2+3+4 = 10.',
     'medio', 13),

    ('¿Qué es un bucle infinito en Java?',
     'a) for(;;)', 'b) for(0)', 'c) while(false)',
     'a', 'for(;;) no tiene condición de parada y crea un bucle infinito.',
     'dificil', 13),

    ('¿Cuántas veces imprime?\nint i = 10;\ndo { System.out.println(i); i++; } while (i < 10);',
     'a) 0', 'b) 1', 'c) 10',
     'b', 'do-while ejecuta primero. Imprime 10, luego i=11 falla la condición. 1 vez.',
     'dificil', 13),

    # ══ JAVA — Funciones (id_tema=14) ═════════════════════════
    ('¿Cómo se llaman las funciones en Java?',
     'a) funciones', 'b) métodos', 'c) procedimientos',
     'b', 'En Java las funciones se llaman métodos y siempre pertenecen a una clase.',
     'facil', 14),

    ('¿Qué significa void en Java?',
     'a) Que el método devuelve null', 'b) Que el método no devuelve nada', 'c) Que es privado',
     'b', 'void indica que el método no tiene valor de retorno.',
     'facil', 14),

    ('¿Cómo se declara un método que devuelve un entero?',
     'a) int miFuncion() {}', 'b) def miFuncion() -> int:', 'c) function miFuncion(): int {}',
     'a', 'En Java se declara el tipo de retorno antes del nombre del método.',
     'facil', 14),

    ('¿Qué es la sobrecarga de métodos en Java?',
     'a) Usar demasiados métodos', 'b) Dos métodos con el mismo nombre pero distintos parámetros', 'c) Heredar métodos',
     'b', 'Java permite métodos con el mismo nombre si difieren en tipo o cantidad de parámetros.',
     'dificil', 14),

    ('¿Qué significa static en un método Java?',
     'a) Que no puede cambiar', 'b) Que pertenece a la clase, no a una instancia', 'c) Que es privado',
     'b', 'Los métodos static se llaman desde la clase directamente, sin crear un objeto.',
     'dificil', 14),

    ('¿Qué imprime?\npublic static int cuadrado(int n) { return n * n; }\nSystem.out.println(cuadrado(4));',
     'a) 4', 'b) 8', 'c) 16',
     'c', 'cuadrado(4) devuelve 4 * 4 = 16.',
     'facil', 14),

    ('¿Qué es la recursión?',
     'a) Un bucle infinito', 'b) Una función que se llama a sí misma', 'c) Un método estático',
     'b', 'La recursión es cuando un método se llama a sí mismo hasta llegar a un caso base.',
     'medio', 14),

    ('¿Qué modificador hace que un método sea accesible solo desde su clase?',
     'a) public', 'b) protected', 'c) private',
     'c', 'private limita el acceso al método a la propia clase donde está definido.',
     'medio', 14),

    ('¿Cuál es el método principal de un programa Java?',
     'a) public void main()', 'b) public static void main(String[] args)', 'c) static main()',
     'b', 'El punto de entrada de todo programa Java es public static void main(String[] args).',
     'medio', 14),

    ('¿Qué hace return en un método Java?',
     'a) Imprime el valor', 'b) Termina el método y devuelve un valor', 'c) Llama al método de nuevo',
     'b', 'return termina la ejecución del método y opcionalmente devuelve un valor.',
     'facil', 14),

    # ══ JAVA — Estructuras de datos (id_tema=15) ══════════════
    ('¿Cómo se declara un array de enteros en Java?',
     'a) int[] arr = {1,2,3};', 'b) array int = [1,2,3];', 'c) int arr = (1,2,3);',
     'a', 'En Java los arrays se declaran con [] después del tipo.',
     'facil', 15),

    ('¿Qué propiedad da la longitud de un array en Java?',
     'a) arr.size()', 'b) arr.length', 'c) len(arr)',
     'b', 'Los arrays en Java tienen la propiedad .length (sin paréntesis).',
     'facil', 15),

    ('¿Qué es un ArrayList en Java?',
     'a) Un array de tamaño fijo', 'b) Una lista dinámica que puede crecer', 'c) Un set sin duplicados',
     'b', 'ArrayList es una lista de tamaño dinámico de la librería java.util.',
     'medio', 15),

    ('¿Cómo se agrega un elemento a un ArrayList?',
     'a) lista.push(elem)', 'b) lista.append(elem)', 'c) lista.add(elem)',
     'c', 'En Java, el método para agregar a una colección es add().',
     'facil', 15),

    ('¿Qué es un HashMap en Java?',
     'a) Un array ordenado', 'b) Una estructura de pares clave-valor', 'c) Un set de enteros',
     'b', 'HashMap almacena pares clave-valor y permite acceso rápido por clave.',
     'medio', 15),

    ('¿Qué es una LinkedList en Java?',
     'a) Una lista con índices', 'b) Una lista donde cada elemento apunta al siguiente', 'c) Un array circular',
     'b', 'LinkedList es una lista enlazada donde cada nodo tiene referencia al siguiente.',
     'dificil', 15),

    ('¿Qué hace Collections.sort(lista) en Java?',
     'a) Invierte la lista', 'b) Ordena la lista', 'c) Elimina duplicados',
     'b', 'Collections.sort() ordena una lista en orden ascendente.',
     'medio', 15),

    ('¿Qué es una Stack en Java?',
     'a) Una lista ordenada', 'b) Una estructura LIFO (último en entrar, primero en salir)', 'c) Una cola',
     'b', 'Stack sigue el principio LIFO. push() agrega y pop() quita el último.',
     'dificil', 15),

    ('¿Qué devuelve lista.size() en Java?',
     'a) El último elemento', 'b) La capacidad máxima', 'c) El número de elementos',
     'c', '.size() devuelve cuántos elementos tiene la colección actualmente.',
     'facil', 15),

    ('¿Qué es una Queue en Java?',
     'a) Una estructura LIFO', 'b) Una estructura FIFO (primero en entrar, primero en salir)', 'c) Un árbol',
     'b', 'Queue es una cola: el primer elemento en entrar es el primero en salir.',
     'dificil', 15),

    # ══ C++ — Variables y tipos de datos (id_tema=16) ═════════
    ('¿Cómo se declara un entero en C++?',
     'a) int x = 5;', 'b) x := 5;', 'c) var x = 5;',
     'a', 'C++ es tipado estático. Se declara el tipo antes del nombre de variable.',
     'facil', 16),

    ('¿Qué librería se incluye para usar cout en C++?',
     'a) #include <stdio>', 'b) #include <iostream>', 'c) #include <output>',
     'b', 'iostream contiene cout para salida y cin para entrada en C++.',
     'facil', 16),

    ('¿Cómo se imprime en C++?',
     'a) print("hola");', 'b) printf("hola");', 'c) cout << "hola";',
     'c', 'cout con el operador << es la forma estándar de imprimir en C++ moderno.',
     'facil', 16),

    ('¿Qué es una variable const en C++?',
     'a) Una variable global', 'b) Una constante que no puede cambiar', 'c) Una variable entera',
     'b', 'const declara una variable cuyo valor no puede modificarse después de inicializar.',
     'medio', 16),

    ('¿Cuál es el tipo para texto de un solo carácter en C++?',
     'a) string', 'b) char', 'c) text',
     'b', 'char almacena un solo carácter. Para texto completo se usa string.',
     'medio', 16),

    ('¿Qué devuelve sizeof(int) en C++ típicamente?',
     'a) 2', 'b) 8', 'c) 4',
     'c', 'int en C++ generalmente ocupa 4 bytes (32 bits) en sistemas modernos.',
     'dificil', 16),

    ('¿Qué es un puntero en C++?',
     'a) Un tipo de dato', 'b) Una variable que guarda la dirección de memoria de otra', 'c) Una referencia constante',
     'b', 'Un puntero almacena la dirección de memoria de otra variable: int* p = &x;',
     'dificil', 16),

    ('¿Qué hace & en int& ref = x?',
     'a) Puntero a x', 'b) Copia de x', 'c) Referencia a x',
     'c', '& en la declaración crea una referencia, un alias de la variable original.',
     'dificil', 16),

    ('¿Qué es auto en C++?',
     'a) Un bucle automático', 'b) Deduce el tipo automáticamente', 'c) Una variable global',
     'b', 'auto hace que el compilador deduzca el tipo basándose en el valor asignado.',
     'medio', 16),

    ('¿Qué imprime cout << 7 / 2?',
     'a) 3.5', 'b) 3', 'c) 4',
     'b', 'La división entre dos enteros en C++ es entera. 7/2 = 3.',
     'medio', 16),

    # ══ C++ — Condicionales (id_tema=17) ══════════════════════
    ('¿Cómo se escribe un if en C++?',
     'a) if x > 5 {', 'b) if (x > 5) {', 'c) if [x > 5]',
     'b', 'En C++ la condición va entre paréntesis y el bloque entre llaves.',
     'facil', 17),

    ('¿Qué operador es AND en C++?',
     'a) and', 'b) &', 'c) &&',
     'c', '&& es el operador AND lógico en C++.',
     'facil', 17),

    ('¿Qué operador es NOT en C++?',
     'a) not', 'b) ~', 'c) !',
     'c', '! es el operador NOT lógico en C++.',
     'facil', 17),

    ('¿Qué es el operador ternario en C++?',
     'a) if/else', 'b) condición ? valorTrue : valorFalse', 'c) switch',
     'b', 'El ternario funciona igual en C++: condición ? siTrue : siFalse.',
     'medio', 17),

    ('¿Qué imprime?\nint x = 4;\nif (x % 2 == 0) cout << "par"; else cout << "impar";',
     'a) impar', 'b) par', 'c) Error',
     'b', 'x=4, 4%2=0, la condición es true, imprime "par".',
     'facil', 17),

    ('¿Qué diferencia hay entre = y == en C++?',
     'a) No hay diferencia', 'b) = asigna, == compara', 'c) == asigna, = compara',
     'b', '= asigna un valor. == compara si dos valores son iguales.',
     'facil', 17),

    ('¿Cuándo usar switch vs if-else en C++?',
     'a) Siempre if-else', 'b) switch cuando se compara una variable contra valores constantes', 'c) switch para rangos',
     'b', 'switch es más limpio cuando se compara una variable contra muchos valores fijos.',
     'medio', 17),

    ('¿Qué pasa sin break en un case de switch en C++?',
     'a) Error', 'b) Fall-through al siguiente case', 'c) Sale del switch',
     'b', 'Sin break ocurre fall-through: ejecuta el siguiente case también.',
     'medio', 17),

    ('¿Qué imprime?\nint x = 15;\ncout << (x > 10 ? "grande" : "pequeño");',
     'a) pequeño', 'b) grande', 'c) Error',
     'b', 'x=15 es mayor que 10, el ternario devuelve "grande".',
     'medio', 17),

    ('¿Qué hace || en C++?',
     'a) OR bit a bit', 'b) OR lógico', 'c) Concatenación',
     'b', '|| es el OR lógico. Devuelve true si al menos una condición es true.',
     'facil', 17),

    # ══ C++ — Bucles (id_tema=18) ══════════════════════════════
    ('¿Cómo se escribe un for básico en C++?',
     'a) for i in range(5)', 'b) for (int i=0; i<5; i++)', 'c) for i = 0 to 5',
     'b', 'El for en C++ tiene: inicialización; condición; incremento.',
     'facil', 18),

    ('¿Qué hace i++ en C++?',
     'a) Decrementa', 'b) Incrementa i en 1', 'c) Multiplica por 2',
     'b', '++ incrementa la variable en 1.',
     'facil', 18),

    ('¿Cómo se itera sobre un vector con for-each en C++?',
     'a) for (int x : v)', 'b) for (x in v)', 'c) foreach (v as x)',
     'a', 'C++11 introdujo el range-based for con los dos puntos :.',
     'medio', 18),

    ('¿Qué hace break en C++?',
     'a) Pausa', 'b) Sale del bucle', 'c) Siguiente iteración',
     'b', 'break termina el bucle o switch inmediatamente.',
     'facil', 18),

    ('¿Cuántas veces itera for(int i=0; i<10; i+=3)?',
     'a) 10', 'b) 3', 'c) 4',
     'c', 'i toma valores 0,3,6,9. Cuando i=12 falla. 4 iteraciones.',
     'medio', 18),

    ('¿Cuál es la diferencia entre while y do-while en C++?',
     'a) No hay', 'b) do-while ejecuta al menos una vez', 'c) while ejecuta siempre',
     'b', 'do-while evalúa la condición al final, por lo que siempre ejecuta al menos una vez.',
     'medio', 18),

    ('¿Qué imprime?\nint s=0; for(int i=1;i<=5;i++) s+=i; cout<<s;',
     'a) 5', 'b) 15', 'c) 10',
     'b', 's acumula 1+2+3+4+5 = 15.',
     'medio', 18),

    ('¿Qué hace continue en C++?',
     'a) Sale del bucle', 'b) Salta a la siguiente iteración', 'c) Pausa',
     'b', 'continue omite el resto del cuerpo y va a la siguiente vuelta.',
     'medio', 18),

    ('¿Qué es un bucle infinito en C++?',
     'a) while(1)', 'b) while(0)', 'c) for(false)',
     'a', 'while(1) siempre es true y crea un bucle infinito.',
     'facil', 18),

    ('¿Cuántas veces imprime?\nint i=1; do { cout<<i; i*=2; } while(i<10);',
     'a) 3', 'b) 4', 'c) 10',
     'b', 'i toma valores 1,2,4,8. Imprime 4 veces. Cuando i=16 falla.',
     'dificil', 18),

    # ══ C++ — Funciones (id_tema=19) ══════════════════════════
    ('¿Cómo se declara una función void en C++?',
     'a) void miFuncion() {}', 'b) def miFuncion():', 'c) function miFuncion() {}',
     'a', 'En C++ se declara el tipo de retorno antes del nombre. void significa sin retorno.',
     'facil', 19),

    ('¿Qué es un prototipo de función en C++?',
     'a) La implementación completa', 'b) La declaración de la función antes de su definición', 'c) Una función abstracta',
     'b', 'El prototipo declara la firma de la función para que pueda usarse antes de definirla.',
     'dificil', 19),

    ('¿Qué imprime?\nint cuadrado(int n) { return n*n; }\ncout << cuadrado(5);',
     'a) 5', 'b) 10', 'c) 25',
     'c', 'cuadrado(5) devuelve 5*5 = 25.',
     'facil', 19),

    ('¿Qué es el paso por referencia en C++?',
     'a) Pasar una copia del valor', 'b) Pasar la dirección para modificar el original', 'c) Pasar un puntero nulo',
     'b', 'void func(int& x) recibe una referencia y puede modificar la variable original.',
     'dificil', 19),

    ('¿Qué es la sobrecarga de funciones en C++?',
     'a) Usar demasiadas funciones', 'b) Funciones con el mismo nombre pero distintos parámetros', 'c) Funciones recursivas',
     'b', 'C++ permite múltiples funciones con el mismo nombre si difieren en sus parámetros.',
     'dificil', 19),

    ('¿Qué es una función inline en C++?',
     'a) Una función anónima', 'b) Una función cuyo código se inserta en el punto de llamada', 'c) Una función estática',
     'b', 'inline sugiere al compilador insertar el cuerpo de la función en cada llamada.',
     'dificil', 19),

    ('¿Qué son los parámetros por defecto en C++?',
     'a) Parámetros obligatorios', 'b) Valores usados si no se pasa argumento', 'c) Parámetros vacíos',
     'b', 'int suma(int a, int b=10) usa 10 para b si no se pasa valor.',
     'medio', 19),

    ('¿Qué devuelve una función con tipo de retorno int sin return?',
     'a) 0', 'b) Comportamiento indefinido', 'c) null',
     'b', 'En C++, omitir return en una función no-void es comportamiento indefinido.',
     'dificil', 19),

    ('¿Qué es la recursión?',
     'a) Un bucle especial', 'b) Una función que se llama a sí misma', 'c) Un puntero a función',
     'b', 'La recursión es cuando una función se llama a sí misma hasta un caso base.',
     'medio', 19),

    ('¿Cuántas veces se llama factorial(3)?',
     'a) 3', 'b) 6', 'c) 4',
     'a', 'factorial(3) llama a factorial(2) que llama a factorial(1). 3 llamadas en total.',
     'dificil', 19),

    # ══ C++ — Estructuras de datos (id_tema=20) ═══════════════
    ('¿Cómo se declara un array en C++?',
     'a) int arr[] = {1,2,3};', 'b) array int = [1,2,3];', 'c) int arr = (1,2,3);',
     'a', 'En C++ los arrays se declaran con [] y se inicializan con {}.',
     'facil', 20),

    ('¿Qué librería se necesita para usar vector en C++?',
     'a) #include <array>', 'b) #include <list>', 'c) #include <vector>',
     'c', 'vector es parte de la STL y requiere #include <vector>.',
     'medio', 20),

    ('¿Qué hace push_back() en un vector?',
     'a) Agrega al inicio', 'b) Elimina el último', 'c) Agrega al final',
     'c', 'push_back() agrega un elemento al final del vector.',
     'facil', 20),

    ('¿Qué es una struct en C++?',
     'a) Una función especial', 'b) Un tipo de dato que agrupa variables', 'c) Un puntero compuesto',
     'b', 'struct define un tipo compuesto con múltiples campos: struct Punto { int x; int y; };',
     'medio', 20),

    ('¿Qué es un map en C++ STL?',
     'a) Una función de transformación', 'b) Una estructura de pares clave-valor ordenada', 'c) Un array asociativo desordenado',
     'b', 'map<K,V> de la STL almacena pares clave-valor ordenados por clave.',
     'dificil', 20),

    ('¿Qué hace v.size() en un vector?',
     'a) Capacidad máxima', 'b) Número de elementos actuales', 'c) Índice del último',
     'b', '.size() devuelve cuántos elementos tiene el vector actualmente.',
     'facil', 20),

    ('¿Qué es un set en C++ STL?',
     'a) Una colección con duplicados', 'b) Una colección sin duplicados y ordenada', 'c) Un array especial',
     'b', 'set<T> almacena elementos únicos ordenados automáticamente.',
     'medio', 20),

    ('¿Qué hace pop_back() en un vector?',
     'a) Agrega al final', 'b) Elimina el primer elemento', 'c) Elimina el último elemento',
     'c', 'pop_back() elimina el último elemento del vector.',
     'medio', 20),

    ('¿Qué es una stack en C++ STL?',
     'a) Una cola', 'b) Una estructura LIFO', 'c) Un vector ordenado',
     'b', 'stack<T> implementa LIFO: push() agrega y pop() quita el último.',
     'dificil', 20),

    ('¿Qué es una queue en C++ STL?',
     'a) Una estructura LIFO', 'b) Un vector desordenado', 'c) Una estructura FIFO',
     'c', 'queue<T> implementa FIFO: push() agrega al final y pop() quita del frente.',
     'dificil', 20),

    # ══ SQL — Consultas básicas (id_tema=21) ══════════════════
    ('¿Qué hace SELECT * FROM tabla?',
     'a) Elimina todos los registros', 'b) Devuelve todas las columnas y filas', 'c) Crea la tabla',
     'b', 'SELECT * selecciona todas las columnas. FROM indica la tabla.',
     'facil', 21),

    ('¿Qué hace INSERT INTO tabla VALUES (...)?',
     'a) Actualiza registros', 'b) Inserta una nueva fila', 'c) Elimina registros',
     'b', 'INSERT INTO agrega una nueva fila a la tabla.',
     'facil', 21),

    ('¿Qué hace UPDATE tabla SET col=val?',
     'a) Inserta filas', 'b) Modifica valores existentes', 'c) Crea columnas',
     'b', 'UPDATE modifica valores en filas existentes.',
     'facil', 21),

    ('¿Qué hace DELETE FROM tabla?',
     'a) Elimina la tabla', 'b) Elimina todas las filas', 'c) Elimina columnas',
     'b', 'DELETE FROM elimina filas. Sin WHERE elimina todas. DROP TABLE elimina la tabla.',
     'medio', 21),

    ('¿Qué hace ORDER BY nombre DESC?',
     'a) Ordena ascendente', 'b) Filtra por nombre', 'c) Ordena descendente',
     'c', 'DESC ordena de mayor a menor. ASC (por defecto) ordena de menor a mayor.',
     'medio', 21),

    ('¿Qué hace LIMIT 5 en una consulta?',
     'a) Salta 5 filas', 'b) Devuelve solo 5 filas', 'c) Filtra 5 columnas',
     'b', 'LIMIT restringe el número de filas devueltas por la consulta.',
     'facil', 21),

    ('¿Qué hace SELECT DISTINCT nombre FROM tabla?',
     'a) Ordena los nombres', 'b) Devuelve nombres sin repetir', 'c) Filtra nombres nulos',
     'b', 'DISTINCT elimina filas duplicadas del resultado.',
     'medio', 21),

    ('¿Qué hace CREATE TABLE en SQL?',
     'a) Inserta datos', 'b) Crea una nueva tabla', 'c) Modifica una tabla',
     'b', 'CREATE TABLE define una nueva tabla con sus columnas y tipos.',
     'facil', 21),

    ('¿Qué hace DROP TABLE en SQL?',
     'a) Vacía la tabla', 'b) Elimina todas las filas', 'c) Elimina la tabla completamente',
     'c', 'DROP TABLE elimina la tabla y todos sus datos de forma permanente.',
     'medio', 21),

    ('¿Qué hace ALTER TABLE en SQL?',
     'a) Elimina la tabla', 'b) Modifica la estructura de la tabla', 'c) Inserta filas',
     'b', 'ALTER TABLE permite agregar, modificar o eliminar columnas de una tabla existente.',
     'medio', 21),

    # ══ SQL — Filtros y condiciones (id_tema=22) ══════════════
    ('¿Qué hace WHERE en SQL?',
     'a) Ordena resultados', 'b) Filtra filas según una condición', 'c) Agrupa resultados',
     'b', 'WHERE filtra las filas que cumplen la condición especificada.',
     'facil', 22),

    ('¿Qué hace LIKE en SQL?',
     'a) Compara igualdad exacta', 'b) Busca patrones en texto', 'c) Compara números',
     'b', "LIKE permite búsquedas con comodines: % para cualquier texto, _ para un carácter.",
     'medio', 22),

    ('¿Qué devuelve WHERE nombre LIKE "A%"?',
     'a) Nombres que terminan en A', 'b) Nombres que contienen A', 'c) Nombres que empiezan con A',
     'c', '% representa cualquier secuencia. "A%" significa empieza con A.',
     'medio', 22),

    ('¿Qué hace BETWEEN en SQL?',
     'a) Une tablas', 'b) Filtra valores en un rango inclusivo', 'c) Filtra nulos',
     'b', 'WHERE edad BETWEEN 18 AND 25 devuelve filas con edad entre 18 y 25 inclusive.',
     'medio', 22),

    ('¿Qué hace IN en SQL?',
     'a) Verifica pertenencia a un conjunto', 'b) Une tablas', 'c) Ordena',
     'a', 'WHERE ciudad IN ("Quito","Ambato") filtra filas donde ciudad sea alguna de las dos.',
     'medio', 22),

    ('¿Qué hace IS NULL en SQL?',
     'a) Compara con cero', 'b) Verifica si un valor es nulo', 'c) Elimina nulos',
     'b', 'IS NULL filtra filas donde el campo no tiene valor (NULL).',
     'facil', 22),

    ('¿Cuál es la diferencia entre WHERE y HAVING?',
     'a) No hay diferencia', 'b) HAVING filtra después de agrupar, WHERE antes', 'c) WHERE agrupa',
     'b', 'WHERE filtra filas antes de GROUP BY. HAVING filtra grupos después de agrupar.',
     'dificil', 22),

    ('¿Qué devuelve NOT IN en SQL?',
     'a) Filas donde el valor está en la lista', 'b) Filas donde el valor NO está en la lista', 'c) Error',
     'b', 'NOT IN es la negación de IN. Devuelve filas cuyo valor no aparece en el conjunto.',
     'medio', 22),

    ('¿Qué hace AND en WHERE?',
     'a) Une tablas', 'b) Requiere que ambas condiciones sean verdaderas', 'c) Filtra duplicados',
     'b', 'AND combina condiciones: todas deben cumplirse para que la fila sea incluida.',
     'facil', 22),

    ('¿Qué hace OR en WHERE?',
     'a) Requiere que todas las condiciones sean verdaderas', 'b) Basta con que una condición sea verdadera', 'c) Niega la condición',
     'b', 'OR incluye la fila si al menos una de las condiciones es verdadera.',
     'facil', 22),

    # ══ SQL — Joins (id_tema=23) ══════════════════════════════
    ('¿Qué hace INNER JOIN en SQL?',
     'a) Devuelve todas las filas de ambas tablas', 'b) Devuelve solo filas con coincidencia en ambas tablas', 'c) Devuelve filas sin coincidencia',
     'b', 'INNER JOIN devuelve solo los registros que tienen coincidencia en ambas tablas.',
     'medio', 23),

    ('¿Qué hace LEFT JOIN en SQL?',
     'a) Devuelve solo la tabla izquierda', 'b) Devuelve todo de la izquierda y coincidencias de la derecha', 'c) Devuelve todo de la derecha',
     'b', 'LEFT JOIN incluye todos los registros de la tabla izquierda, con NULL donde no hay coincidencia.',
     'medio', 23),

    ('¿Qué hace RIGHT JOIN en SQL?',
     'a) Devuelve todo de la derecha y coincidencias de la izquierda', 'b) Solo tabla derecha', 'c) Solo coincidencias',
     'a', 'RIGHT JOIN incluye todos los registros de la tabla derecha, con NULL donde no hay coincidencia.',
     'medio', 23),

    ('¿Qué hace FULL OUTER JOIN?',
     'a) Solo coincidencias', 'b) Todo de ambas tablas con NULL donde no hay coincidencia', 'c) Producto cartesiano',
     'b', 'FULL OUTER JOIN combina LEFT y RIGHT JOIN: devuelve todo de ambas tablas.',
     'dificil', 23),

    ('¿Qué es una clave foránea (FOREIGN KEY)?',
     'a) Una clave duplicada', 'b) Una columna que referencia la clave primaria de otra tabla', 'c) Un índice especial',
     'b', 'FOREIGN KEY establece la relación entre dos tablas.',
     'medio', 23),

    ('¿Qué hace ON en un JOIN?',
     'a) Ordena el resultado', 'b) Especifica la condición de unión', 'c) Filtra nulos',
     'b', 'ON define cómo se relacionan las tablas: ON tabla1.id = tabla2.id_tabla1.',
     'facil', 23),

    ('¿Qué es un CROSS JOIN?',
     'a) Une por claves', 'b) Producto cartesiano de dos tablas', 'c) Filtra duplicados',
     'b', 'CROSS JOIN combina cada fila de una tabla con cada fila de la otra.',
     'dificil', 23),

    ('¿Cuándo usar LEFT JOIN en lugar de INNER JOIN?',
     'a) Cuando se quieren solo coincidencias', 'b) Cuando se quieren todos los registros aunque no haya coincidencia', 'c) Para ordenar',
     'b', 'LEFT JOIN es útil cuando quieres todos los registros de la tabla principal aunque no tengan datos relacionados.',
     'dificil', 23),

    ('¿Qué devuelve un JOIN sin condición ON?',
     'a) Error siempre', 'b) Solo la primera tabla', 'c) El producto cartesiano',
     'c', 'Sin ON, el JOIN combina todas las filas de una tabla con todas las de la otra.',
     'dificil', 23),

    ('¿Qué es un SELF JOIN?',
     'a) Un join de una tabla consigo misma', 'b) Un join sin condición', 'c) Un join de tres tablas',
     'a', 'SELF JOIN une una tabla con ella misma usando alias para distinguirlas.',
     'dificil', 23),

    # ══ SQL — Funciones de agregación (id_tema=24) ════════════
    ('¿Qué hace COUNT(*) en SQL?',
     'a) Suma los valores', 'b) Cuenta el número de filas', 'c) Promedia los valores',
     'b', 'COUNT(*) cuenta cuántas filas hay en el resultado.',
     'facil', 24),

    ('¿Qué hace SUM(columna) en SQL?',
     'a) Cuenta filas', 'b) Promedia valores', 'c) Suma todos los valores de la columna',
     'c', 'SUM() suma todos los valores numéricos de la columna especificada.',
     'facil', 24),

    ('¿Qué hace AVG(columna) en SQL?',
     'a) Devuelve el máximo', 'b) Calcula el promedio', 'c) Cuenta valores distintos',
     'b', 'AVG() calcula el promedio (media aritmética) de los valores.',
     'facil', 24),

    ('¿Qué hace MAX(columna) en SQL?',
     'a) Devuelve el promedio', 'b) Devuelve el valor mínimo', 'c) Devuelve el valor máximo',
     'c', 'MAX() devuelve el valor más alto de la columna.',
     'facil', 24),

    ('¿Qué hace GROUP BY en SQL?',
     'a) Ordena resultados', 'b) Agrupa filas con el mismo valor para aplicar funciones de agregación', 'c) Filtra grupos',
     'b', 'GROUP BY agrupa filas con el mismo valor en una columna.',
     'medio', 24),

    ('¿Qué hace HAVING en SQL?',
     'a) Filtra filas antes de agrupar', 'b) Filtra grupos después de GROUP BY', 'c) Ordena grupos',
     'b', 'HAVING es el WHERE de los grupos: filtra después de aplicar GROUP BY.',
     'medio', 24),

    ('¿Qué devuelve COUNT(DISTINCT nombre)?',
     'a) Total de filas', 'b) Nombres distintos sin contar repetidos', 'c) Suma de nombres',
     'b', 'COUNT(DISTINCT col) cuenta cuántos valores únicos hay en la columna.',
     'dificil', 24),

    ('¿Qué hace MIN(columna)?',
     'a) Devuelve el promedio', 'b) Devuelve el máximo', 'c) Devuelve el valor mínimo',
     'c', 'MIN() devuelve el valor más bajo de la columna.',
     'facil', 24),

    ('¿Puede usarse WHERE con funciones de agregación?',
     'a) Sí siempre', 'b) No, para eso existe HAVING', 'c) Solo con COUNT',
     'b', 'WHERE no puede filtrar por funciones de agregación. Para eso se usa HAVING.',
     'dificil', 24),

    ('¿Qué devuelve GROUP BY departamento con COUNT(*)?',
     'a) Un solo número', 'b) El número de filas por cada departamento', 'c) Los nombres de departamento',
     'b', 'GROUP BY + COUNT(*) devuelve una fila por grupo con el conteo de registros.',
     'medio', 24),

    # ══ SQL — Subconsultas (id_tema=25) ═══════════════════════
    ('¿Qué es una subconsulta en SQL?',
     'a) Una tabla temporal', 'b) Una consulta dentro de otra consulta', 'c) Un tipo de JOIN',
     'b', 'Una subconsulta es un SELECT anidado dentro de otro SELECT, WHERE o FROM.',
     'medio', 25),

    ('¿Dónde puede aparecer una subconsulta?',
     'a) Solo en WHERE', 'b) En SELECT, FROM o WHERE', 'c) Solo en FROM',
     'b', 'Las subconsultas pueden usarse en SELECT, FROM y WHERE.',
     'medio', 25),

    ('¿Qué hace EXISTS en SQL?',
     'a) Verifica si una tabla existe', 'b) Devuelve true si la subconsulta devuelve al menos una fila', 'c) Cuenta filas',
     'b', 'EXISTS devuelve true si la subconsulta tiene algún resultado.',
     'dificil', 25),

    ('¿Qué hace IN con una subconsulta?',
     'a) Une tablas', 'b) Verifica si el valor está en el resultado de la subconsulta', 'c) Filtra nulos',
     'b', 'WHERE id IN (SELECT id FROM ...) filtra filas cuyo id esté en el resultado.',
     'medio', 25),

    ('¿Qué es una subconsulta correlacionada?',
     'a) Una subconsulta independiente', 'b) Una subconsulta que referencia la consulta externa', 'c) Una subconsulta en FROM',
     'b', 'Una subconsulta correlacionada usa valores de la consulta externa, ejecutándose por cada fila.',
     'dificil', 25),

    ('¿Qué es una CTE (Common Table Expression)?',
     'a) Un tipo de JOIN', 'b) Una subconsulta nombrada definida con WITH', 'c) Una función de agregación',
     'b', 'WITH nombre AS (SELECT ...) define una CTE que puede usarse como tabla en la consulta.',
     'dificil', 25),

    ('¿Qué ventaja tiene una CTE sobre una subconsulta?',
     'a) Es más rápida siempre', 'b) Es más legible y puede reutilizarse en la misma consulta', 'c) Puede modificar datos',
     'b', 'Las CTEs hacen el código más legible y evitan repetir subconsultas complejas.',
     'dificil', 25),

    ('¿Qué hace NOT EXISTS?',
     'a) Devuelve true si la subconsulta tiene filas', 'b) Devuelve true si la subconsulta NO tiene filas', 'c) Elimina filas',
     'b', 'NOT EXISTS es la negación de EXISTS: true cuando la subconsulta no devuelve resultados.',
     'dificil', 25),

    ('¿Puede una subconsulta devolver múltiples columnas?',
     'a) No, solo una', 'b) Sí, siempre', 'c) Depende de dónde se use',
     'c', 'En WHERE generalmente devuelve una columna. En FROM puede devolver múltiples.',
     'dificil', 25),

    ('¿Qué hace ALL en SQL?',
     'a) Selecciona todo', 'b) Compara un valor contra todos los resultados de una subconsulta', 'c) Une tablas',
     'b', 'WHERE salario > ALL (SELECT salario FROM ...) filtra donde el salario supera a todos.',
     'dificil', 25),
]

con.executemany(
    'INSERT INTO ejercicios(pregunta,opcion_a,opcion_b,opcion_c,respuesta_correcta,explicacion,dificultad,id_tema) VALUES(?,?,?,?,?,?,?,?)',
    ejercicios
)
con.commit()
con.close()
print(f'{len(ejercicios)} ejercicios insertados correctamente.')