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

# Iteraciones (*Loops*)

En las actividades anteriores, realizamos algunas operaciones simples con Python. Es sumamente importante aprender a realizar estas acciones, pero adquieren relevancia cuando nos sirven para hacer una tarea repetitiva.

Por ejemplo, supongamos que tenemos la cadena de caracteres con los Estados y Capitales de México:

```{code-cell} ipython3
estados = "Aguascalientes: Aguascalientes, Baja California: Mexicali, Baja California Sur: La Paz, Campeche: Campeche, Chiapas: Tuxla Gutiérrez, Chihuahua: Chihuahua, Ciudad de México: Ciudad de México, Coahuila de Zaragoza: Saltillo, Colima: Colima, Durango: Durango, Estado de México: Toluca de Lerdo, Guanajuato: Guanajuato, Hidalgo: Pachuca de Soto, Jalisco: Guadalajara, Michoacán: Morelia, Morelos: Cuernavaca, Nayarit: Tepic, Nuevo León: Monterrey, Oaxaca: Oaxaca de Juárez, Puebla: Puebla de Zaragoza, Querétaro: Santiago de Querétaro, Quintana Roo: Chetumal, San Luis Potosí: San Luis Potosí, Sinaloa: Culiacán, Sonora: Hermosillo, Tabasco: Villahermosa, Tamaulipas: Ciudad Victoria, Tlaxcala: Tlaxcala, Veracruz: Xalapa, Yucatán: Mérida, Zacatecas: Zacatecas"
```

Si queremos separar los estados y capitales, podemos hacerlo de la siguiente manera:

```{code-cell} ipython3
estados = estados.split(", ")
```

Con este método, estamos separando (*split*) la cadena de caracteres de acuerdo con un delimitador (*", "*). Esto nos da como resultado una lista. Cada uno de los elementos obtenidos es una cadena de caracteres que contiene un estado y su capital.

Ahora, necesitaremos separar cada uno de estos elementos en dos cadenas de caracteres, una para el estado y otra para la capital. Para esto, podemos utilizar el método *split* de nuevo, pero esta vez con un delimitador diferente (*":"*).

El problema está en que si aplico esto a la lista en general me dará un error:

```{code-cell} ipython3
estados = estados.split(": ")
```

Por esa razón, tendré que aplicar a cada uno de los elementos de la lista esta separación. Podemos hacerlo caso por caso, pero esto sería muy tedioso. Para ello, utilizaremos un *for loop*.

## For loops

Un *for loop* es una estructura de control que nos permite repetir una acción un número determinado de veces. En Python, se utiliza la palabra reservada *for* para indicar que se va a realizar una iteración.

Apliquemos esta idea en la lista de Estados y capitales:

```{code-cell} ipython3
for estado in estados:
    estado = estado.split(": ")
    print(estado)
```

Vemos que cada uno de los elementos de la lista se ha separado en un listado de dos elementos. El primer elemento corresponde al Estado y el segundo a su capital.

Podríamos, por lo tanto, separar cada uno de estos elementos en dos variables y asignarle una categoría textual para describir su contenido:

```{code-cell} ipython3
for estado in estados:
    estado = estado.split(": ")
    estado[0] = "Estado: " + estado[0]
    estado[1] = "Capital: " + estado[1]
    print(estado)
```

Incluso, podemos crear un diccionario, para que de esa manera podamos acceder a los elementos de manera más sencilla:

```{code-cell} ipython3
estados_dict = {}

for estado in estados:
    estado = estado.split(": ")
    estados_dict[estado[0]] = estado[1]

print(estados_dict)
```

En este caso, si quisiera saber la capital de un estado, puedo hacerlo de la siguiente manera:

```{code-cell} ipython3
estados_dict["Chiapas"]
```

Vamos a ver con más detalle qué hicimos en el ejercicio anterior.

### Iteración sobre una lista

En el ejemplo anterior, iteramos sobre una lista. Esto significa que, para cada uno de los elementos de la lista, se ejecutó el código que se encuentra dentro del *for loop*.

Es decir, es como si hubiéramos escrito el código de la siguiente manera:

```{code-cell} ipython3
estado1 = estados[0]
estado1 = estado1.split(": ")
estado1[0] = "Estado: " + estado1[0]
estado1[1] = "Capital: " + estado1[1]
print(estado1)

estado2 = estados[1]
estado2 = estado2.split(": ")
estado2[0] = "Estado: " + estado2[0]
estado2[1] = "Capital: " + estado2[1]
print(estado2)

# y así sucesivamente

```

Claramente, escribir el código de esa manera no sería para nada práctico, de hecho sería más lento y difícil que hacerlo a mano directamente.

Las iteraciones o *loops* son una herramienta muy poderosa que nos permite automatizar procesos repetitivos y hacerlos más eficientes.

## Crear listas a partir de iteraciones

Supongamos que no queremos separar los elementos de la lista, sino recuperar únicamente los elementos que corresponden a las capitales de los Estados. En este caso, lo que haremos será crear una lista vacía y agregar a esta lista cada una de las capitales que se encuentren en la lista de Estados y capitales.

```{code-cell} ipython3
capitales = []

for estado in estados:
    estado = estado.split(": ")
    capitales.append(estado[1])

print(capitales)
```

Esta es una tarea muy recurrida y que nos puede servir para separar elementos a partir de un identificador común. Por ejemplo, si tenemos una lista de nombres de personas y queremos separar los nombres de los apellidos, podemos hacerlo de la siguiente manera:

```{code-cell} ipython3
nombres = ["Juan Pérez", "María López", "Pedro Pérez", "Ana García", "José Hernández", "María Martínez", "Pedro García", "Ana Hernández", "José Martínez", "María Pérez"]

apellidos = []

for nombre in nombres:
    nombre = nombre.split(" ")
    apellidos.append(nombre[1])

print(apellidos)
```

Y con esta lista, podemos hacer una operación como contar cuántas veces se repite cada apellido:

```{code-cell} ipython3
from collections import Counter

Counter(apellidos)
```

Los *for loops* son una herramienta tan ampliamente utilizada que incluso se recomienda no utilizarlos cuando no sea necesario, ya que pueden hacer que el código sea más lento.

## Listas de comprensión

Esta es un concepto un poquito más avanzado, pero que es muy útil para crear listas a partir de iteraciones. En lugar de crear una lista vacía y agregar elementos a esta lista, podemos crear una lista a partir de una iteración.

```{code-cell} ipython3
capitales = [estado.split(": ")[1] for estado in estados]

print(capitales)
```

Realizamos exactamente la misma tarea que en el ejercicio anterior, pero ahorramos unas cuantas líneas de código. Básicamente tomamos la declaración del loop (`for estado in estados`) y la pasamos al "final" de la lista. A la vez, pusimos en primer lugar la operación que haremos con la iteración [`estado.split(": "](1)`). Para que funcione, ponemos esta operación entre corchetes (`[]`).

No toda iteración puede escribirse de esta manera, pero en general se hace con aquella que implican una operación sencilla.

No esperamos que domines inmediatamente este concepto, pero estoy seguro que lo encontrarás en ejemplos y en tutoriales de Python, por eso es bueno que lo tengas en cuenta.

## While loops

Los *while loops* son otra estrategia para realizar iteraciones. En general, son menos utilizados que los *for loops*, pero pueden ser muy útiles en ciertas situaciones. Por ejemplo, cuando no sabemos cuántas veces se va a repetir un proceso.

Los *while loops* se ejecutan mientras una condición sea verdadera. Por ejemplo, si queremos imprimir los números del 1 al 10, podemos hacerlo de la siguiente manera:

```{code-cell} ipython3
i = 1

while i <= 10:
    print(i)
    i += 1
```

En este caso, la condición es que `i` sea menor o igual a 10. En cada iteración, se imprime el valor de `i` y se le suma 1. Cuando `i` ya no es menor o igual a 10, el *while loop* se detiene.

```{admonition} Precaución
:class: warning

Es importante que en cada iteración se modifique la variable que se utiliza en la condición, de lo contrario el *while loop* se ejecutará indefinidamente. Eso es lo que se denomina como un *loop infinito*.
```

## Síntesis

Estos son algunos de los aspectos básicos de las iteraciones en Python. En general, recurriremos a ellas de manera continua porque son uno de los fundamentos de la programación.

En el siguiente segmento, veremos los condicionales, que combinados con los *loops* nos permitirán crear programas más complejos.
