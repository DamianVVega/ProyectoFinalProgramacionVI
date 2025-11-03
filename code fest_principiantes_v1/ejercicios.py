EJERCICIOS = {
    "facil": [
        {
            "id": 1,
            "titulo": "El Famoso FIZZ BUZZ.",
            "descripcion": "Escribe un programa que muestre por consola (con un print) los número de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:\nMúltiplos de 3 por la palabra 'fizz'.\nMúltiplos de 5 por la palabra 'buzz'.\nMúltiplos de 3 y de 5 a la vez por la palabra 'fizzbuzz'.",
            "duracion": 20,
            "puntaje": 10,
            "codigo": "482917",
            "estado": "sin resolver",
            "temas_relacionados": "condicionales, ciclo for", 
            "pista1": """ Usa un bucle for del 1 al 100 y condicionales con el operador módulo (%) para
            saber si el número es múltiplo de 3, 5 o ambos""",
            "pista2": """ El orden de los if importa: si primero verificas 3 o 5, podrías perder el caso de
            ambos; piensa en comprobar el caso “fizzbuzz” antes que los demás. """
        },
        {
            "id": 2,
            "titulo": "Impar, Par",
            "descripcion": "Crea un programa donde se debe ingresar un número entero, imprime si es par, impar además de primo.",
            "duracion": 20,
            "puntaje": 10,
            "codigo": "193064",
            "estado": "sin resolver",
            "temas_relacionados": "condicionales, operaciones matemáticas",
            "pista1": """ Usa n % 2 para determinar si es par o impar """,
            "pista2": """ Supongamos que tienes el número ingresado en una variable, luego con una condicional tienes que preguntar si
                            esa variable modulo 2 da exacto 0, solamente seria multiplo 2/par, caso contrario es impar""" 
        },
        {
            "id": 3,
            "titulo": "Tabla de Multiplicar.",
            "descripcion": "Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10",
            "duracion": 20,
            "puntaje": 10,
            "codigo": "750231",
            "estado": "sin resolver",
            "temas_relacionados": "bucles, entrada y salida de datos",
            "pista1": """ Utiliza un bucle for del 1 al 10, y en cada iteración multiplica el número
            ingresado. """,
            "pista2": """ Muestra el proceso completo, por ejemplo: "5 x 3 = 15", para hacerlo más claro
            y legible. """ 
        }
    ],
    "intermedio": [
        {
            "id": 1,
            "titulo": "Número de Armstrong(o Narcisista)",
            "descripcion": " Un número de Armstrong es un número entero que es igual a la suma de sus propios dígitos, elevados cada uno a la potencia del número total de dígitos que tiene.\nEjemplo: \n153 es un número Armstrong, \ncomo se calcula eso? \nSe suma cada uno de sus dígitos, elevados a la cantidad de dígitos que tienen. \nLos dígitos son 1,5 y 3, y la cantidad de dígitos es 3. Por lo tanto, la resolución quedaría de la siguiente manera: \n1^3+5^3+3^3=1+125+27=153.",
            "duracion": 30,
            "puntaje": 20,
            "codigo": "608547",
            "estado": "sin resolver",
            "temas_relacionados": "bucles, manipulación de cadenas",
            "pista1": """ Convierte el número en cadena para recorrer sus dígitos y conocer cuánto de
            longitud tiene.""",
            "pista2": """  Eleva cada dígito a la cantidad de dígitos totales (Longitud) y suma los resultados;
            si la suma es igual al número original, es un numero de Armstrong. """ 
        },
        {
            "id": 2,
            "titulo": "Invertir cadena.",
            "descripcion": " Ingrese una palabra y imprima la palabra invertida, sin el uso de funcionalidades propias del lenguaje de programación utilizado.",
            "duracion": 30,
            "puntaje": 20,
            "codigo": "912386",
            "estado": "sin resolver",
            "temas_relacionados": "cadenas, bucles",
            "pista1": """ Usa un bucle for que empiece desde el último carácter hasta el primero,concatenando manualmente.""",
            "pista2": """ Cuando quieras recorrer una cadena o lista de fin a inicio, recuerda que un bucle
            for tiene tres partes: inicio, fin y paso.
            • Inicio: el índice desde donde comienzas (último elemento de la cadena).
            • Fin: hasta dónde quieres llegar (normalmente antes del primer elemento, porque
            el índice final no se incluye).
            • Paso: cuánto avanzas en cada iteración; para ir hacia atrás, este valor debe ser: ? """ 
        },
        {
            "id": 3,
            "titulo": "Palíndromo.",
            "descripcion": "Ingrese una palabra, e imprima si se lee de un sentido que el del otro.",
            "duracion": 30,
            "puntaje": 20,
            "codigo": "347520",
            "estado": "sin resolver",
            "temas_relacionados": "cadenas, comparación de valores",
            "pista1": """ Si ya resolviste el ejercicio de invertir cadena, este debe ser pan comido (como
            que 3 líneas de código más jeje) """,
            "pista2": """Cuando quieras recorrer una cadena o lista de fin a inicio, recuerda que un
            bucle for tiene tres partes: inicio, fin y paso.
            • Inicio: el índice desde donde comienzas (último elemento de la cadena).
            • Fin: hasta dónde quieres llegar (normalmente antes del primer elemento, porque
            el índice final no se incluye).
            • Paso: cuánto avanzas en cada iteración; para ir hacia atrás, este valor debe ser: ? """ 
        }
    ],
    "dificil": [
        {
            "id": 1,
            "titulo": "A prueba de errores.",
            "descripcion": "Crea un programa que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres.\nEl programa debe encontrarlos y retornarlos en formato lista/array.\n• Ambas cadenas de texto deben ser iguales en longitud.\n• Las cadenas de texto son iguales elemento a elemento.\n• No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente.\nEjemplos:\n- Me llamo jose / Me llemo joso -> ['e','o']\n- Me llamo lujan / Me llamo lujih -> ['i', 'h']\nRecomendación: al pedir las dos cadenas al usuario, trata de que la segunda sea la errónea.",
            "duracion": 40,
            "puntaje": 35,
            "codigo": "826415",
            "estado": "sin resolver",
            "temas_relacionados": "comparación de cadenas, bucles",
            "pista1": """ Prueba recorriendo un for hasta una de las longitudes de las cadenas, luego
            adentro puedes hacer tu consulta si los elementos son iguales o no, con un if. """,
            "pista2": """ usa el i(elemento iterativo del for), como referencia para verificar los
            elementos de las dos cadenas al mismo tiempo.
            Ejemplo: if cadena[i] no es igual cadena2[i] """ 
        },
        {
            "id": 2,
            "titulo": "El Cajero Automático",
            "descripcion": """
            Cree un programa que simule el funcionamiento básico de un cajero automático.
            El programa deberá permitir las siguientes opciones:
            Consultar saldo
            Depositar dinero
            Retirar dinero
            Salir del sistema
            Requisitos:
            El saldo inicial será de 0.
            Cuando se realice un depósito, el monto se sumará al saldo.
            Cuando se realice un retiro:
            Verifique si hay suficiente saldo.
            Si no lo hay, muestre un mensaje de error.
            El programa debe ejecutarse en un bucle (menú) hasta que el usuario elija salir.
            Valide que los montos ingresados sean números positivos.
            """,
            "duracion": 40,
            "puntaje": 35,
            "codigo": "570893",
            "estado": "sin resolver",
            "temas_relacionados": "condicionales, bucles",
            "pista1": """
            Usá un bucle para que el menú se repita hasta que el usuario decida salir, y una variable global o externa para mantener el saldo entre operaciones.
            """,
            "pista2": """ 
                    Uso de condicionales por cada opción, para depositar plata simplemente concatena el valor agregado al saldo global, y para retirar preguntar primero si el saldo global es mayor a lo que quieres retirar 
            """ 
        },
        {
            "id": 3,
            "titulo": "Sistema de participantes Code Fest.",
            "descripcion": """ Crea un programa que simule el mecanismo de participación del codefest:\n
            Mediante la terminal, el programa te preguntará si quieres añadir, borrar participantes, mostrarlos o salir.\n
            - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter, añadiéndolo.\n
            - Si seleccionas añadir un participante, y este ya existe, avisarás de ello. (Y no lo duplicarás)\n
            - Si seleccionas mostrar los participantes, se listarán todos.\n
            - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter. (Avisando de si lo has eliminado o el nombre no existe)\n
            - Por cada acción (Añadir, eliminar, mostrar, preguntar al usuario si desea seguir usándolo, si es asi, mostrar de nuevo el menú principal)\n
            - Si seleccionas salir, el programa finalizará. """,
            "duracion": 40,
            "puntaje": 35,
            "codigo": "264179",
            "estado": "sin resolver",
            "temas_relacionados": "listas, manejo de entradas y condicionales",
            "pista1": """ 
            Usa una lista para guardar los nombres, y un bucle while True para mostrar el menú (añadir, eliminar, mostrar, salir) las veces que prefiera el usuario o si prefieres, has una función que ejecute todo tu código las veces que sean necesarias.(Al preguntar si desea seguir usando el programa)
            Lo difícil del ejercicio es saber como preguntar si un elemento existe o no en una lista, aplica para añadir o eliminar un participante.
            Puedes hacerlo con un ciclo for, recorriendo la lista hasta que encuentres o no el elemento introducido por el usuario, la forma de encontrarlo es usando la condicional if
            """,
            "pista2": """ 
            if lista[i] == participante:
                            # El participante ya existe (no añadir de nuevo o avisar que no se puede eliminar)
                            else:
                            # Si no coincide con ningún elemento, se puede añadir o eliminar sin problema
            """ 
        }
    ]
}
