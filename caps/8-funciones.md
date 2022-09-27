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

También podemos determinar un valor por defecto para los argumentos de una función. En este caso, si no se especifica un valor para el argumento, se utilizará el valor por defecto:

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

En este caso, la función se comporta de acuerdo con los nuevos valores que le estamos pasando.

## Notas

[^clases]: Obviamente, apenas hemos arañado la superficie. Con estos elementos es posible hacer programas de diferentes niveles. Sin embargo, para poder abarcar un conocimiento básico de Python, también es importante tener en cuenta que existen otros elementos que no hemos visto en este curso. En particular, las clases son un tipo de objeto complejo y permiten crear estructuras de programación más completas. En caso de que quieras profundizar en el tema, te recomiendo mucho el capítulo 9 de {cite}`matthes_python_2016`.
