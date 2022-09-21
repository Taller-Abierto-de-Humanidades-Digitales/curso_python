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

# Un curso rapidísimo de Python

Este es un curso rapidísimo de Python, diseñado para empezar a familiarizarte con el mundo de la programación. Vamos a tratar de comprender algunos conceptos básicos de la programación, y a escribir nuestro primer programa.

## ¿Qué es Python?

Python es un [lenguaje de programación de alto nivel](https://sites.google.com/site/teoriadelenguajesycompiladores/aplicaciones-de-la-tecnologia-de-compiladores/implementacion-de-lenguajes-de-programacion-de-alto-nivel), es decir, que traduce nuestras instrucciones a la computadora para que pueda ejecutar las acciones que le pedimos.

Python tiene otra ventaja y es que es un lenguaje interpretado, lo que quiere decir que nuestros programas no necesitan compilarse para ser ejecutados. Esto hace que sea muchísimo más sencillo de aprender que otros lenguajes de programación.

Finalmente, y esto es algo muy atractivo para quienes no nos dedicamos a la ciencia de la computación, es un lenguaje cuya sintaxis es muy sencilla y fácil de aprender. De hecho, muchas de las instrucciones son sumamente intuitivas. Por eso se dice que el lenguaje de Python es expresivo, porque con una sola instrucción podemos lograr mucho. Solamente para dar un ejemplo, en un lenguaje como C, para imprimir un mensaje en pantalla, tendríamos que escribir:

```c
#include <stdio.h>
int main() {
   printf("¡Hola mundo!");
   return 0;
}
```

Esto sin contar que el programa tiene que se compilado para que se pueda ejecutar.

```{code-cell} ipython3
from subprocess import call
call(["../holamundo.h"]) # <- Este es el programa de arriba compilado en C
```

En Python, la misma tarea se puede lograr con una sola línea de código:

```{code-cell}
print("Hola mundo")
```

El resultado que ves arriba es resultado de ejecutar el código anterior. Por esa razón, Python es un lenguaje con tanta popularidad, porque es muy fácil de aprender y de usar.

## ¿Qué es un programa?

Un programa es una secuencia de instrucciones que siguen un orden lógico para lograr un objetivo. Por ejemplo, si yo quiero que mi computadora "salude" a una persona por su nombre y apellido, puedo escribir un programa que haga eso. En Python, el programa se vería así:

```{code-cell}
nombre = "Francisco"
apellido = "Azimov"
print("Hola", nombre, apellido)
```

En este caso, el programa tiene tres instrucciones:

1. Asignar el valor "Juan" a la variable `nombre`.
2. Asignar el valor "Pérez" a la variable `apellido`.
3. Imprimir el mensaje "Hola" seguido del valor de las variables `nombre` y `apellido`.

Vamos a explorar más sobre las variables un poco más adelante. Por lo pronto, es suficiente con que tengas en cuenta que la computadora no entiende valores complejos, y en las humanidades (paradójicamente) vivimos en un mundo de complejidad. Por eso, necesitamos que la computadora entienda los conceptos que nosotros queremos analizar y esos valores se asignan a variables.

Programar nos sirve para automatizar tareas que realizamos de manera repetitiva y a procesar grandes cantidades de información de manera muy rápida. En este microcurso, vamos a realizar operaciones muy acotadas, de tal manera que puedas ver y comprender cada paso, pero en la vida real, los programas son mucho más complejos.

## Entonces ¿qué es codificar?

Codificar consiste en escribir un programa con un lenguaje de programación. Los términos programación y codificación suelen usarse de manera intercambiable, pero programar es un proceso mucho más amplio. Programar consiste en escribir un programa, pero también en probarlo, depurarlo, documentarlo, etc. En este curso, vamos a aprender a codificar, pero no vamos a entrar en detalles sobre el resto de los pasos.

## Y ¿en dónde entran los algoritmos?

Los algoritmos son una serie de pasos que se siguen para resolver un problema. Por ejemplo, si quiero saber cuánto es 2 + 2, puedo escribir un algoritmo que me diga el resultado. En este caso, el algoritmo sería:

1. Tomar el número 2.
2. Sumarle el número 2.
3. Imprimir el resultado.

En Python, el algoritmo se vería así:

```{code-cell}
print(2 + 2)
```

Fácil, ¿no? Pero generalmente no nos encontramos con problemas que ya han sido resueltos de manera tan sencilla. Por ejemplo, si tenemos la frase "Más vale un pájaro en la mano que dos volando", ¿cómo podemos saber cuántas palabras tiene? Podemos escribir un algoritmo que nos ayude a resolver este problema. En este caso, el algoritmo sería:

1. Contar el número de espacios en la frase.
2. Sumarle 1 al resultado anterior.

En Python, el algoritmo se vería así:

```{code-cell}
frase = "Más vale un pájaro en la mano que dos volando"
espacios = frase.count(" ")
palabras = espacios + 1
print(palabras)
```

Como habrás notado, este algoritmo parte de la respuesta a una pregunta ¿qué es una palabra? La respuesta que tomamos es que una palabra es una secuencia de caracteres separada por espacios. En este sentido, si se identifica el valor común (espacios) y se cuenta cuántas veces aparece, se puede saber cuántas palabras hay en la frase. En este caso, el resultado es 9. También sabemos que toda frase tiene un espacio menos que palabras (porque no termina en espacio), por eso se suma 1 al resultado.

Obviamente este es un algoritmo muy simple, y ya habrás deducido otra gran cantidad de posibilidades de error. Por ejemplo, ¿qué sucede si la frase termina en un espacio? ¿Cómo podemos lidiar con signos de puntuación? ¿Podemos considerar como palabras a las conjunciones? Involucrar estas preguntas en el algoritmo es lo que va construyendo un programa y lo hace más sofisticado. Por esta razón, es relevante entender que un algoritmo es un conjunto de instrucciones simples que, en conjunto, pueden resolver una cantidad casi infinita de problemas.

## En síntesis

* El algoritmo es una serie de pasos que se siguen para resolver un problema.
* El programa es una secuencia de instrucciones que siguen un orden lógico para lograr un objetivo.
* La codificación es escribir un programa con un lenguaje de programación.

Ahora que tenemos los primeros conceptos claros, pongámonos manos a la obra.
