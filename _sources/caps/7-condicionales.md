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

# Condicionales

Los condicionales nos permiten evaluar la verdad o falsedad lógica de una expresión para tomar decisiones en nuestro código. En Python, los condicionales se escriben con la palabra reservada `if` y se cierran con la palabra reservada `else`.

```{code-cell} ipython3
if 1 == 1:
    print("1 es igual a 1")
else:
    print("1 no es igual a 1")
```

Como en todos los casos, estas condiciones también pueden ser aplicadas a texto:

```{code-cell} ipython3

nombre = "Ana"

if nombre == "Juan":
    print("Hola, Juan")
else:
    print("Hola, tu no eres Juan")
```

Incluso, esta condición se puede realizar de manera que determine si la condición es falsa:

```{code-cell} ipython3
if nombre != "Juan":
    print("Hola, Ana")
else:
    print("Hola, Juan")
```

Por otra parte, un condicional nos puede ayudar a modificar el valor de una variable de acuerdo con ciertas condiciones. Por ejemplo, en el siguiente caso queremos que la variable `nombre` tome el valor de "Juan" si el valor de la variable `edad` es mayor a 18, y que tome el valor de "Ana" si el valor de la variable `edad` es menor a 18.

```{code-cell} ipython3

edad = 20

if edad > 18:
    nombre = "Juan"
else:
    nombre = "Ana"

print(nombre)
```

## Condicionales + listas + iteraciones

Los condicionales también pueden ser utilizados en conjunto con listas y iteraciones. Por ejemplo, supongamos que tenemos una lista de nombres y queremos separar los nombres que empiezan con la letra "A" de los que no. Para esto, podemos crear dos listas vacías y agregar a cada una de ellas los nombres que empiecen con la letra "A" y los que no, respectivamente.

```{code-cell} ipython3

nombres = ["Ana", "Juan", "Pedro", "Andrea", "Sofía", "Antonio"]

nombres_con_a = []
nombres_sin_a = []

for nombre in nombres:
    if nombre[0] == "A":
        nombres_con_a.append(nombre)
    else:
        nombres_sin_a.append(nombre)

print(nombres_con_a)
print(nombres_sin_a)
```

En el caso anterior, utilizamos muchos de los conceptos que hemos visto hasta ahora. Por ejemplo, utilizamos la iteración `for` para recorrer la lista de nombres, y utilizamos la condición `if` para determinar si el nombre empieza con la letra "A" o no, para lo cual recurrimos a una segmentación de la cadena de caracteres. Además, utilizamos la función `append` para agregar elementos a las listas `nombres_con_a` y `nombres_sin_a`.

Podríamos hacer otro tipo de operaciones similares y un poco más compleja, por ejemplo, encontrar los años en una frase textual. Para esto, podemos utilizar la función `split` para separar la frase en palabras y luego iterar sobre cada una de ellas para determinar si es un número o no.

```{code-cell} ipython3

frase = "En el año 2020, el mundo se enfrentó a una pandemia que cambió la vida de todos."

palabras = frase.split()

años = []

for palabra in palabras:
  palabra = palabra.replace(',', '')
  if palabra.isnumeric():
    años.append(palabra)

años
```

En el caso anterior, utilizamos la función `replace` para eliminar la coma de la palabra "2020," y luego utilizamos la función `isnumeric` para determinar si la palabra es un número o no. Solamente en los casos en los que el resultado es verdadero, agregamos la palabra a la lista `años`.

Este caso es sencillo, pero intentemos con uno un poco más complejo. Supongamos que queremos extraer las fechas de una pequeña biografía de [Cervantes Saavedra](https://es.wikipedia.org/wiki/Miguel_de_Cervantes#Infancia_y_juventud):

```{code-cell} ipython3
bio = "El padre del escritor era Rodrigo de Cervantes (1509-1585), casado con Leonor de Cortinas, de la cual apenas se sabe nada, excepto que era natural de Arganda del Rey.11​ Los hermanos de Cervantes fueron Andrés (1543), Andrea (1544), Luisa (1546), que llegó a ser priora de un convento carmelita; Rodrigo (1550), también soldado, que le acompañó en el cautiverio argelino; Magdalena (1554) y Juan, solo conocido porque su padre lo menciona en el testamento."
```

Para conseguir lo anterior, debemos realizar varias operaciones:

1. Separar la biografía en palabras (`split()`).
2. Eliminar la puntuación de cada palabra (`replace()`). De otra manera, no identificaría una fecha como "(1543)".
3. En caso de que la palabra tenga el formato "AAAA-AAAA", separarla en dos palabras (`split('-')`) y agregar ambas a la lista de fechas (`append()`).
4. Determinar si la palabra es un número (`isnumeric()`).
5. Agregar la palabra a la lista de fechas (`append()`).

```{code-cell} ipython3

palabras = bio.split()

palabras = bio.split()

fechas = []

for palabra in palabras:
  palabra = palabra.replace(',', '')
  palabra = palabra.replace(';', '')
  palabra = palabra.replace('(', '')
  palabra = palabra.replace(')', '')
  palabra = palabra.replace('​', '')
  palabra = palabra.replace('11', '') # Esto se podría hacer de manera más "elegante", pero por ahora funciona.
  if palabra.isnumeric():
    fechas.append(palabra)
  elif '-' in palabra: # Esto es un condicional anidado.
    rango = palabra.split('-') # Esto es una segmentación.
    for r in rango: # Esto es una iteración anidada.
      if r.isnumeric(): 
        fechas.append(r)

fechas
```

Vemos que gracias a los condicionales podemos realizar operaciones más complejas, incluso cuando no tenemos todavía claro qué resultado vamos a obtener. De hecho, podríamos simplemente ampliar o cambiar el párrafo que utilizamos y encontraríamos las fechas de la nueva biografía.

```{admonition} Próximamente
:class: tip

En una próxima sesión veremos cómo replicar el código a través de funciones. Esto nos permitirá reutilizar nuestro código en múltiples ocasiones.
```

## Condicionales  + diccionarios

Los condicionales también pueden ser utilizados en conjunto con diccionarios. Por ejemplo, supongamos que tenemos un diccionario con los nombres de los alumnos de un curso y sus notas. Queremos saber cuál es la nota más alta y cuál es la nota más baja. Para esto, podemos crear dos variables, una para la nota más alta y otra para la nota más baja, y luego iterar sobre el diccionario para determinar si la nota es mayor o menor que la nota más alta o más baja, respectivamente.

```{code-cell} ipython3

notas = {"Ana": 7, "Juan": 5, "Pedro": 8, "Andrea": 9, "Sofía": 6, "Antonio": 4}

nota_mas_alta = 0
nota_mas_baja = 10

for alumno, nota in notas.items(): # Iteramos sobre el diccionario
  if nota > nota_mas_alta:
    nota_mas_alta = nota
  if nota < nota_mas_baja:
    nota_mas_baja = nota

print("La nota más alta es", nota_mas_alta)
print("La nota más baja es", nota_mas_baja)
```

En el caso anterior, utilizamos dos condicionales `if` para determinar si la nota es mayor o menor que la nota más alta o más baja, respectivamente. En el caso de que la nota sea mayor que la nota más alta, actualizamos la variable `nota_mas_alta` con el valor de la nota. De forma similar, en el caso de que la nota sea menor que la nota más baja, actualizamos la variable `nota_mas_baja` con el valor de la nota.

De una manera similar, podríamos hacer un programa que saludara a cada usuario y determinara si la persona es de género fenemino ("Bienvenida"), masculino ("Bienvenido") o no binario ("Bienvenidx").

```{code-cell} ipython3

usuarios = {"Ana": "Femenino", "Juan": "Masculino", "Pedro": "No binario", "Andrea": "Femenino", "Sofía": "Femenino", "Antonio": "Masculino"}

for usuario, genero in usuarios.items():
  if genero == "Femenino":
    print("Bienvenida", usuario)
  elif genero == "Masculino":
    print("Bienvenido", usuario)
  else:
    print("Bienvenidx", usuario)
```

Esta es una de las grandes utilidades del diccionario, que nos evita la ambigüedad o el generar condiciones lógicas más complejas para determinar si un usuario es de género femenino, masculino o no binario.

## Condicionales + listas múltiples

En ciertas ocasiones, vamos a querer saber si ciertos elementos de una lista están contenidos en otra. Por ejemplo, si tenemos dos grupos de estudiantes, queremos saber cuáles estudiantes se encuentran inscritos en ambos grupos:

```{code-cell} ipython3

grupo_1 = ["Ana", "Juan", "Pedro", "Andrea", "Sofía", "Antonio"]
grupo_2 = ["Ana", "Juan", "Pedro", "Andrea", "Sofía", "Antonio", "María", "Luis"]

inscritos_ambos_grupos = []

for estudiante in grupo_1:
  if estudiante in grupo_2:
    inscritos_ambos_grupos.append(estudiante)

print(inscritos_ambos_grupos)
```

En general, esta no es una operación muy común. En general se suelen utilizar otros métodos un tanto más sofisticados para determinar si dos listas comparten elementos. Sin embargo, es importante tener en cuenta que esta operación es posible.

## Síntesis

En esta sección, vimos cómo los condicionales son útiles para encontrar condiciones de verdad que permiten que el flujo del programa tome una dirección particular. En general, con los aspectos que hemos visto hasta ahora es suficiente para poder construir nuestros primeros programas. Sin embargo, nos hace falta una herramienta fundamental para poder programar con toda seguridad: las funciones.
