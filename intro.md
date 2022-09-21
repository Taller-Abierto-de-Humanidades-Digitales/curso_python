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

Python es un lenguaje de programación de alto nivel, es decir, que traduce nuestras instrucciones a la computadora para que pueda ejecutar las acciones que le pedimos. Un lenguaje de bajo nivel es aquel que está más cerca de la máquina, y por lo tanto, es más difícil de aprender.

Python tiene otra ventaja y es que es un lenguaje interpretado, lo que quiere decir que nuestros programas no necesitan compilarse para ser ejecutados. Esto hace que sea muchísimo más sencillo de aprender que otros lenguajes de programación.

Finalmente, y esto es algo muy atractivo para quienes no nos dedicamos a la ciencia de la computación, es un lenguaje cuya sintaxis es muy sencilla y fácil de aprender. De hecho, muchas de las instrucciones son sumamente intuitivas. Por eso se dice que el lenguaje de Python es expresivo, porque con una sola instrucción podemos lograr mucho. Solamente para dar un ejemplo, en un lenguaje como C, para imprimir un mensaje en pantalla, tendríamos que escribir:

```c
#include <stdio.h>
int main() {
   printf("¡Hola mundo!");
   return 0;
}
```

Esto sin contar que el programa tiene que se compilado para que se pueda ejecutar. En Python, la misma tarea se puede lograr con una sola línea de código:

```{code-cell}
print("Hola mundo")
```

El resultado que ves arriba es resultado de ejecutar el código anterior. Por esa razón, Python es un lenguaje con tanta popularidad, porque es muy fácil de aprender y de usar.

## ¿Qué es un programa?

Un programa es una secuencia de instrucciones que siguen un orden lógico para lograr un objetivo. Por ejemplo, si yo quiero que mi computadora "salude" a una persona por su nombre y apellido, puedo escribir un programa que haga eso. En Python, el programa se vería así:

```{code-cell}
nombre = "Juan"
apellido = "Pérez"
print("Hola", nombre, apellido)
```

En este caso, el programa tiene tres instrucciones:

1. Asignar el valor "Juan" a la variable `nombre`.
2. Asignar el valor "Pérez" a la variable `apellido`.
3. Imprimir el mensaje "Hola" seguido del valor de las variables `nombre` y `apellido`.

Vamos a explorar más sobre las variables un poco más adelante. Por lo pronto, es suficiente con que tengas en cuenta que la computadora no entiende valores complejos, y en las humanidades (paradójicamente) vivimos en un mundo de complejidad. Por eso, necesitamos que la computadora entienda los conceptos que nosotros queremos analizar.

Programar nos sirve para automatizar tareas que realizamos de manera repetitiva y a procesar grandes cantidades de información de manera muy rápida. En las ciencias, Python se ha convertido en un lenguaje de programación con mucha popularidad, y es el más usado en el mundo de la ciencia de datos.



+++

```{tableofcontents}
```
