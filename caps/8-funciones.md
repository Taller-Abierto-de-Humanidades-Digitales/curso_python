---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Funciones

Vamos a finalizar nuestro curso intensivo con una de las herramientas más poderosas de Python: las funciones [^clases].

En términos simples, las funciones son bloques de código que realizan una tarea específica y pueden ser reutilizadas en diferentes partes de nuestro programa "llamándolas" por su nombre.

Por ejemplo, ¿recuerdas el programa que creamos para saludar a alguien de acuerdo con su nombre y género? Podríamos escribirlo de la siguiente manera:

```{code-cell} ipython3

def saludar(nombre, genero):
    """Saluda a alguien de acuerdo con su nombre y género"""
    if genero == "f":
        print(f"¡Bienvenida, {nombre}!")
    elif genero == "m":
        print(f"¡Bienvenido, {nombre}!")
    else:
        print(f"¡Bienvenidx, {nombre}!")

saludar("María", "f")
```

Detengámonos un poco en la sintaxis de este código.

En primer lugar, debemos tener en cuenta que una función se define con la palabra reservada `def` seguida del nombre de la función y de los argumentos que recibe entre paréntesis. En este caso, la función `saludar` recibe dos argumentos: `nombre` y `genero`.

La cantidad de argumentos que recibe una función no es fija. De hecho, podemos crear una función sin argumentos:

```{code-cell} ipython3

def saludar():
    """Solamente, saluda"""
    print("¡Hola!")

saludar()
```

O con muchos argumentos:

```{code-cell} ipython3

def saludar(nombre, genero, edad, ciudad):
    """Saluda a alguien de acuerdo con su nombre, género, edad y ciudad"""
    if genero == "f":
        print(f"¡Bienvenida, {nombre}!")
    elif genero == "m":
        print(f"¡Bienvenido, {nombre}!")
    else:
        print(f"¡Bienvenidx, {nombre}!")
    print(f"Veo que tienes {edad} años y vives en {ciudad}.")

saludar("María", "f", 25, "Buenos Aires")
```

También podemos determinar un valor predeterminado para los argumentos de una función. En este caso, si no se especifica un valor para el argumento, se utilizará el valor asignado:

```{code-cell} ipython3

def saludar(nombre, genero, edad=25, ciudad="Buenos Aires"):
    """Saluda a alguien de acuerdo con su nombre, género, edad y ciudad"""
    if genero == "f":
        print(f"¡Bienvenida, {nombre}!")
    elif genero == "m":
        print(f"¡Bienvenido, {nombre}!")
    else:
        print(f"¡Bienvenidx, {nombre}!")
    print(f"Veo que tienes {edad} años y vives en {ciudad}.")

saludar("María", "f")
```

En este caso, el argumento `edad` toma el valor por defecto de 25 y el argumento `ciudad` toma el valor por defecto de "Buenos Aires". Si especificamos un valor para alguno de estos argumentos, se utilizará el valor que le pasamos:

```{code-cell} ipython3

saludar("Laura", "f", 30, "Ciudad de México")
```

Vemos ahora como la función se comporta de acuerdo con los nuevos valores que le estamos pasando.

## Retorno de valores

En los ejemplos anteriores, cada función es un programa que termina con la instrucción `print`. No obstante, en la vida real, las funciones se utilizan sobre todo para transformar los datos que reciben y devolver un resultado. Para ello, la función tiene la palabra reservada `return` que indica el valor que se devuelve:

```{code-cell} ipython3

def saludar(nombre, genero):
    """Saluda a alguien de acuerdo con su nombre y género"""
    if genero == "f":
        return f"¡Bienvenida, {nombre}!"
    elif genero == "m":
        return f"¡Bienvenido, {nombre}!"
    else:
        return f"¡Bienvenidx, {nombre}!"

saludo = saludar("María", "f")
print(saludo)
```

El comportamiento es similar al de la función `print`, pero en este caso, el valor que devuelve la función se almacena en la variable `saludo` y luego se imprime.

Esta es una función sumamente simple, que no tiene una utilidad mayor, pero nos permite entender el concepto de retorno de valores.

Es importante entender que una función puede retornar cualquier tipo de valor, incluyendo listas o diccionarios. ¿Recuerdas el ejemplo del condicional que nos permitía extraer las fechas de una corta biografía? En ese caso, podríamos escribir una función que haga lo mismo con cualquier biografía:

```{note}
La lógica de esta función viene determinada por el tipo de información que le estamos pasando al programa. En este caso, sabemos que las fechas se escriben completas (AAAA) y que no contamos con valores decimales que nos puedan confundir (p. ej, en "1894.45" el primer valor - 1894 - es una fecha y el segundo valor - 45 - es un llamado a una nota al pie). Es por tanto una función hecha a propósito para este caso particular.
```

```{code-cell} ipython3

def extraer_fechas(biografia):
    """
    Extrae las fechas de una biografía
    Es posible sintetizar mucho más esta función, pero la escribimos de esta manera para leer mejor cada paso
    """

    bio = biografia.split(" ") # Separamos la biografía en palabras
    fechas = []
    for palabra in bio:
        # eliminamos los signos de puntuación excepto puntos y guiones
        palabra = palabra.strip(",;:()[]{}") # el método strip elimina los caracteres que le indicamos al inicio o al final de la cadena
        if palabra.endswith("."): # el método endswith verifica si la cadena termina con el caracter que le indicamos
          palabra = palabra.replace(".", "")

        if len(palabra) > 3 and palabra.isdigit():
          fechas.append(int(palabra)) # el método append agrega un elemento a la lista
        elif len(palabra) > 5 and "-" in palabra: # <-- aquí estamos buscando fechas escritas como AAAA-AAAA
          separar_palabras = palabra.split("-")
          for sp in separar_palabras:
            if sp.isdigit() and len(sp) > 3:
              fechas.append(int(sp))
        elif len(palabra) > 5 and "." in palabra: # <-- aquí estamos buscando valores numéricos que tengan un punto en el medio
          separar_palabras = palabra.split(".")
          for sp in separar_palabras:
            if sp.isdigit() and len(sp) > 3:
              fechas.append(int(sp))
    
    return fechas # devolvemos la lista de fechas
```

Con esta función, ya no tenemos que limitarnos a una biografía, sino que podemos extraer las fechas de cualquier biografía:

```{code-cell} ipython3

# Tomamos el primer párrafo de la biografía en español de Wikipedia

Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4​ 29 de septiembre de 1547-Madrid, 22 de abril3​ de 1616) fue un novelista, poeta, dramaturgo y soldado español."
Quevedo = "Francisco Gómez de Quevedo Villegas y Santibáñez Cevallos (Madrid, 14 de septiembre de 1580-Villanueva de los Infantes, Ciudad Real, 8 de septiembre de 1645) fue un noble, político y escritor español del Siglo de Oro."
Calderon = "Pedro Calderón de la Barca (Madrid, 17 de enero de 1600-25 de mayo de 1681) fue un escritor español, sacerdote católico, miembro de la Venerable Congregación de Presbíteros Seculares Naturales de Madrid San Pedro Apóstol y caballero de la Orden de Santiago, conocido fundamentalmente por ser uno de los más insignes literatos barrocos del Siglo de Oro, en especial por su teatro."

bios = [Cervantes, Quevedo, Calderon]

for b in bios:
  fechas = extraer_fechas(b)
  print(fechas)

```

Vemos que en este caso, la función devuelve una lista de fechas, que luego podemos utilizar para realizar cualquier tipo de análisis.

## Escribir código de manera sucinta

Nuestra función `extraer_fechas()` funciona sin problemas. Sin embargo, esto no significa que esté bien escrita. Dicha función sufre de un mal que se denomina "verborrea" (en inglés lo encontrarás mucho como *verbose*), es decir, escribir con muchas más instrucciones, variables, valores, etc; de los necesarios.

La idea siempre es intentar escribir la menor cantidad de líneas de código posible. Esto en general se consigue si se utilizan expresiones regulares. Estas consisten en secuencias de caracteres que especifican patrones de búsqueda en un texto. Por ejemplo, si quiero buscar en un texto todas las coincidencias de 4 dígitos, en lugar de recurrir a condicionales como en la función de ejemplo, utilizaremos la expresión regular `\b\d{4}\b`, que se puede entender como:

- `\d`: cualquier dígito entre 0 y 9
- `{4}`: cuantificador que nos indica coincidencias de 4 caracteres del mismo tipo.
- `\b`: delimitador de palabra, que indica al programa que solamente busque cadenas de cuatro dígitos que estén rodeadas por caracteres que no sean dígitos (evita así que se seleccionen números de más de 4 dígitos)

Haciendo uso de esta técnica (y de la librería [re](https://docs.python.org/3/library/re.html#module-re)), es posible reducir nuestra función a una línea:

```{code-cell} ipython3
import re

def extraer_fechas(biografia):
    '''
    biografia (str) párrafo con una biografía de Wikipedia
    '''
    # usar el patrón regular para encontrar todas las fechas en la biografía
    return re.compile(r"\b\d{4}\b").findall(biografia)
```

Después de ver la reducción radical que tuvo nuestra función podríamos incluso dudar en usarla. Sin embargo, debido a que se puede utilizar muchas veces a lo largo de un programa, es más sencillo modificar una sola línea y que se afecte todo el programa.

Las expresiones regulares son muy útiles, pero también representa cierta complejidad entender su lenguaje formal. Afortunadamente abundan las guías y manuales que abordan este tema.

## Síntesis

Hemos visto algunos de los aspectos básicos de las funciones en Python. En particular, hemos visto cómo definir una función, cómo pasarle argumentos y cómo devolver un valor. Puedes notar que en este lenguaje de programación, es bastante simple definir funciones y construir las propias.

Básicamente, con los conceptos que hemos visto hasta ahora podemos construir programas de cierta complejidad, todo depende del problema que queramos resolver y de los datos que tengamos disponibles.

## Notas

[^clases]: Obviamente, apenas hemos arañado la superficie. Con estos elementos es posible hacer programas de diferentes niveles. Sin embargo, para poder abarcar un conocimiento básico de Python, también es importante tener en cuenta que existen otros elementos que no hemos visto en este curso. En particular, las clases son un tipo de objeto complejo y permiten crear estructuras de programación más completas. En caso de que quieras profundizar en el tema, te recomiendo mucho el capítulo 9 de {cite}`matthes_python_2016`.
