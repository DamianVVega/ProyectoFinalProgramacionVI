EJERCICIOS = {
    "facil": [
        {
            "id": 1,
            "titulo": "Calentamiento",
            "descripcion": "Escribe un programa que reciba una oración, y pueda guardar cada palabra de ella como elemento de una lista, luego imprime esa lista.(Se acepta uso de funcionalidades propias  de tu lenguaje de programación utilizado)",
            "duracion": 15,
            "puntaje": 10,
            "codigo": "482917",
            "estado": "sin resolver",
            "temas_relacionados": "condicionales, ciclo for", 
            "pista1": """
            Si no sabes de funcionalidades propias de tu lenguaje, tendras que hacerlo de forma manual con un for ;)
            """,
            "pista2": """ 
            Usa el espacio a tu favor, ya estando dentro del for, puedes ir añadiendo los caracteres de la frase dentro de una variable mientras no encuentres un espacio, pero cuando lo encuentres, todo lo que estuviste añadiendo anteriormente, lo agregas como elemento a la lista, repitiendo el mismo proceso una y otra vez, tendras un problema con la ultima palabra pero espero puedas resolverlo.
            """
        },
        {
            "id": 2,
            "titulo": "Invertir Cadena.",
            "descripcion": "Ingrese una palabra y imprima la palabra invertida, sin el uso de funcionalidades propias del lenguaje de programación utilizado.",
            "duracion": 15,
            "puntaje": 10,
            "codigo": "193064",
            "estado": "sin resolver",
            "temas_relacionados": "condicionales, operaciones matemáticas",
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
            "titulo": "Número de Armstrong.",
            "descripcion": """ 
            Un número de Armstrong es un número entero que es igual a la suma de sus propios dígitos, elevados cada uno a la potencia del número total de dígitos que tiene.\nEjemplo: \n153 es un número Armstrong, \ncomo se calcula eso? \nSe suma cada uno de sus dígitos, elevados a la cantidad de dígitos que tienen. \nLos dígitos son 1,5 y 3, y la cantidad de dígitos es 3. Por lo tanto, la resolución quedaría de la siguiente manera: \n1^3+5^3+3^3=1+125+27=153.
            """,
            "duracion": 15,
            "puntaje": 10,
            "codigo": "750231",
            "estado": "sin resolver",
            "temas_relacionados": "bucles, entrada y salida de datos",
            "pista1": """ Convierte el número en cadena para recorrer sus dígitos y conocer cuánto de
            longitud tiene.""",
            "pista2": """  Eleva cada dígito a la cantidad de dígitos totales (Longitud) y suma los resultados;
            si la suma es igual al número original, es un numero de Armstrong. """ 
        }
    ],
    "intermedio": [
        {
            "id": 1,
            "titulo": "Faltantes",
            "descripcion": "Dado un array de enteros ordenado y sin repetidos, crea un programa que calcule y imprima todos los que faltan entre el mayor y el menor. Ejemplo de input",
            "duracion": 25,
            "puntaje": 20,
            "codigo": "608547",
            "estado": "sin resolver",
            "temas_relacionados": "bucles, manipulación de cadenas",
            "pista1": """ Usa un bucle for para recorrer desde el número menor hasta el mayor del array. Puedes obtenerlos con array[0] y array[-1]. """,
            "pista2": """ Dentro del bucle, utiliza otra estructura for que recorra el array original y verifique si el número actual existe o no.  """ 
        },
        {
            "id": 2,
            "titulo": "Sistema de participantes Code Fest.",
            "descripcion": """ Crea un programa que simule el mecanismo de participación del codefest:\n
            Mediante la terminal, el programa te preguntará si quieres añadir, borrar participantes, mostrarlos o salir.\n
            - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter, añadiéndolo.\n
            - Si seleccionas añadir un participante, y este ya existe, avisarás de ello. (Y no lo duplicarás)\n
            - Si seleccionas mostrar los participantes, se listarán todos.\n
            - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter. (Avisando de si lo has eliminado o el nombre no existe)\n
            - Por cada acción (Añadir, eliminar, mostrar, preguntar al usuario si desea seguir usándolo, si es asi, mostrar de nuevo el menú principal)\n
            - Si seleccionas salir, el programa finalizará. """,
            "duracion": 25,
            "puntaje": 20,
            "codigo": "912386",
            "estado": "sin resolver",
            "temas_relacionados": "cadenas, bucles",
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
        },
        {
            "id": 3,
            "titulo": "Cifrado César.",
            "descripcion": """ 
            Crea un programa que realice el cifrado César de un texto y lo imprima.\nEl programa deberá pedir la cadena a cifrar y el número de posiciones que será desplazado.\n¿Qué es el cifrado césar?\nEs una de las técnicas de cifrado más simples y más usadas. Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
            \nPor ejemplo, con un desplazamiento de 3, la a sería sustituida por la d (situada 3 lugares a la derecha de la a), la b sería reemplazada por la e, etc.
            \nEjemplo: Si se ingresa abc como cadena a cifrar, y el valor 3 como numero de desplazamientos, el resultado obtenido sería def.
            \nSe les proporcionara el abecedario ya que lo estarán necesitando ;) :
            \na, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z
            - Pueden usar el cifrado simplemente en minúsculas para evitarse la fatiga jeje.
            """,
            "duracion": 25,
            "puntaje": 20,
            "codigo": "347520",
            "estado": "sin resolver",
            "temas_relacionados": "cadenas, comparación de valores",
            "pista1": """Al ingresar la cadena, trata de recorrer cada elemento de ella, en ese lapso,
            busca cada elemento de ella dentro del abecedario, una vez encontrado, debes
            moverte n pasos de desplazamiento, y ese es el elemento que sustituirá al elemento de
            la cadena. """,
            "pista2": """ 
                Siguiendo la anterior pista:
                a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z
                Si yo ingreso “abc” como cadena de prueba, y elijo 3 como valor de desplazamiento,
                quedaría de la siguiente manera la codificación:
                Cadena normal:
                a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z
                Codificado (Cadena desplazada):
                a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z
                a se movió 3 pasos, los demás lo mismo.
                Para lograr esto en programación, lo más optimo es realizar un doble ciclo for, uno
                dentro de otro:
                For:
                                   For:
                El primero recorrerá la cadena, y el segundo el abecedario, entonces adentro del
                segundo for, lo único que tienes que hacer es:
                Encontrar el elemento de la cadena, dentro del abecedario, una vez hecho eso, a esa
                ubicación, que debe estar por índice, sumarle el numero de desplazamiento, ese
                elemento será el que sustituya al elemento de la cadena, lo añades a una nueva
                cadena, y repites el proceso por cada elemento.            
            """  
        }
    ],
    "dificil": [
        {
            "id": 1,
            "titulo": "Fibonacci",
            "descripcion": """ 
            /*
            * Escribe un programa que imprima los 50 primeros números de la sucesión
            * de Fibonacci empezando en 0.
            * - La serie Fibonacci se compone por una sucesión de números en
            *   la que el siguiente siempre es la suma de los dos anteriores.
            *   0, 1, 1, 2, 3, 5, 8, 13...
            */
            """,
            "duracion": 35,
            "puntaje": 35,
            "codigo": "826415",
            "estado": "sin resolver",
            "temas_relacionados": "comparación de cadenas, bucles",
            "pista1": """ 
            Pensá cómo podrías generar el siguiente número de la serie a partir de los dos anteriores.  
            ¿Qué dos valores iniciales deberías usar para empezar la secuencia?
            """,
            "pista2": """  
            Empezá con dos variables que representen los dos primeros valores: 0 y 1.  
            Luego, dentro de un bucle, mostrás el primer valor y calculás el siguiente sumando ambos.  
            Después, desplazá los valores para continuar el ciclo.  
            Ejemplo lógico: siguiente = primero + segundo → luego primero = segundo, segundo = siguiente.
            """ 
        },
        {
            "id": 2,
            "titulo": "Contador de vocales y consonantes",
            "descripcion":""" 
            Pide una palabra o frase y muestra cuántas vocales y consonantes contiene.
            """,
            "duracion": 35,
            "puntaje": 35,
            "codigo": "570893",
            "estado": "sin resolver",
            "temas_relacionados": "cadenas, listas y bucles anidados",
            "pista1": """ 
            Recordá que las vocales son: a, e, i, o, u.  
            Intentá recorrer la palabra y verificar si cada letra coincide con alguna de esas vocales.
            """,
            "pista2": """       
            Recorre cada carácter de la palabra.  
            Si es igual a 'a', 'e', 'i', 'o' o 'u', sumá uno al contador de vocales.  
            Si no coincide con ninguna de ellas y es una letra, sumá uno al contador de consonantes.  
            Podés ignorar los espacios y otros símbolos.
            """ 
        },
        {
            "id": 3,
            "titulo": "Contador de letras y números",
            "descripcion": """ 
            Pide una cadena y cuenta cuántos caracteres son letras y cuántos son números.
            """,
            "duracion": 35,
            "puntaje": 35,
            "codigo": "264179",
            "estado": "sin resolver",
            "temas_relacionados": "listas, manejo de entradas y condicionales",
            "pista1": """ 
            Pensá que las letras van de 'a' a 'z' y los números del '0' al '9'.  
            Podés comparar cada carácter con esos rangos para decidir a qué tipo pertenece.
            """,
            "pista2": """  
            Recorre la cadena carácter por carácter.  
            Si el carácter está entre '0' y '9', contalo como número.  
            Si está entre 'a' y 'z' o 'A' y 'Z', contalo como letra.  
            Evitá contar espacios u otros símbolos.
            """ 
        }
    ]
}
