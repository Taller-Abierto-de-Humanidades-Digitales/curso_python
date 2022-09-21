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

# Listas

Ya vimos valores asignados individualmente a una variable. Esto realmente no es muy útil. Lo que nos interesa es poder guardar varios valores en una sola variable. Para esto, utilizamos las listas.

Las listas se definen como una colección de elementos en un orden en particular. En Python, las listas son conjuntos de muchos tipos de datos, incluyendo números, cadenas de texto, booleanos, etc.

Las listas se definen con corchetes `[]` y los elementos se separan con comas `,`. Por ejemplo, una lista con los protagonistas de la serie de televisión "Friends" se puede definir como:

```{code-cell} ipython3
protagonistas = ["Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"]
protagonistas
```

## Accediendo a los elementos de una lista

Para acceder a los elementos de una lista, utilizamos el índice del elemento. Los índices de las listas comienzan en 0, por lo que el primer elemento de la lista es el elemento con índice 0. Por ejemplo, para acceder al primer elemento de la lista `protagonistas`, utilizamos el índice 0:

```{code-cell} ipython3
protagonistas[0]
```

De la misma manera podemos acceder a cualquier elemento de la lista. Siempre que conozcamos su ubicación, podemos acceder a un resultado esperado. Por ejemplo, para acceder a `"Joey"`, utilizamos el índice 3:

```{code-cell} ipython3
protagonistas[3]
```

Incluso, podemos saber si `"Chandler"` está en la lista:

```{code-cell} ipython3
"Chandler" in protagonistas
```

Podemos utilizar un valor de la lista para asignarlo a una variable, por ejemplo, para incluirlo en una frase:

```{code-cell} ipython3
print(f"{protagonistas[0]} es una de las protagonista de la serie Friends")
```

Estas son operaciones muy básicas con las listas, pero son fundamentales para poder utilizarlas.

## Modificando los elementos de una lista

Podemos modificar los elementos de una lista. Por ejemplo, podemos cambiar el nombre de la primera protagonista de la serie:

```{code-cell} ipython3
protagonistas[0] = "Rachel Green"
protagonistas
```

Notarás que inmediatamente cambia la lista. Esto es porque las listas son mutables, es decir, podemos modificarlas.

Podríamos querer realizar lo mismo con otro de los caracteres, por ejemplo con `"Joey"`:

```{code-cell} ipython3
protagonistas[3] = "Joey Tribbiani"
protagonistas
```

Es decir, de manera básica, si conocemos la posición del valor, podemos modificarlo. Posteriormente veremos cómo utilizar condicionales para modificar los valores de una manera más dinámica.

## Agregando elementos a una lista

Podemos agregar elementos a una lista, para ello utilizamos el método `append()`. Por ejemplo, podemos agregar a la lista a un nuevo personaje de la serie:

```{code-cell} ipython3
protagonistas.append("Gunther")
protagonistas
```

En el caso de `append()` el elemento se asignará siempre al final de la lista. Si queremos agregar un elemento en una posición específica, utilizamos el método `insert()`. Por ejemplo, podemos agregar a la lista a un nuevo personaje de la serie al lado de `"Chandler"`:

```{code-cell} ipython3
protagonistas.insert(5, "Janice")
protagonistas
```

En general se suele utilizar con mucha mayor frecuencia el método `append()`, esto porque en general la lista se va llenando de elementos y no se suele agregar en una posición específica.

## Eliminando elementos de una lista

Podemos eliminar elementos de una lista, para ello utilizamos el método `remove()`. Por ejemplo, podemos eliminar a `"Gunther"` de la lista:

```{code-cell} ipython3
protagonistas.remove("Gunther")
protagonistas
```

Si queremos eliminar un elemento en una posición específica, utilizamos el método `pop()`. Por ejemplo, podemos eliminar a `"Janice"` de la lista:

```{code-cell} ipython3
protagonistas.pop(5)
protagonistas
```

Como verás, el método `remove()` es mucho más intuitivo y en general es más utilizado que `pop()`.

## Ordenando una lista

Podemos ordenar una lista, para ello utilizamos el método `sort()`. Por ejemplo, podemos ordenar la lista de los protagonistas de la serie:

```{code-cell} ipython3
protagonistas.sort()
protagonistas
```

Obviamente, aquí debemos tener en cuenta que la forma de ordenar los elementos depende del tipo de datos que se esté utilizando. Por ejemplo, si tenemos una lista de números, se ordenará de menor a mayor. Si tenemos una lista de cadenas de texto, se ordenará alfabéticamente.

```{admonition} Orden alfabético y mayúsculas
:class: tip
El orden de la lista se realiza alfabéticamente, por lo que las mayúsculas tienen prioridad sobre las minúsculas. Por ejemplo, `"A"` es menor que `"a"`. Esto es importante tenerlo en cuenta, ya que puede generar resultados inesperados.
```

Esto implica que también podemos ordenar de manera inversa, para ello utilizamos el método `sort(reverse=True)`. Por ejemplo, podemos ordenar la lista de los protagonistas de la serie de manera inversa:

```{code-cell} ipython3
protagonistas.sort(reverse=True)
protagonistas
```

Existe otro método de reordenación de una lista que es `reverse()`. Este método invierte el orden de los elementos de la lista. Por ejemplo, podemos invertir el orden de la lista de los protagonistas de la serie:

```{code-cell} ipython3
protagonistas.reverse()
protagonistas
```

En este caso, la lista no está ordenada "alfabéticamente", sino que se invierte el orden de los elementos. Por ejemplo:

```{code-cell} ipython3
lista = [1, 3, 5, 7, 5]
lista.reverse()
lista
```

## Longitud de una lista

Finalmente, una operación muy recurrida es hallar el número de elementos de una lista. Para ello utilizamos la función `len()`. Por ejemplo, podemos hallar el número de elementos de la lista de los protagonistas de la serie:

```{code-cell} ipython3
len(protagonistas)
```

Y así podemos utilizarlo en otras variables, como en la frase:

```{code-cell} ipython3
print(f'Los protagonistas de Friends son {len(protagonistas)}')
```

En este momento es básicamente un asunto de curiosidad, pero cuando veámos los bucles, veremos que es muy útil para saber cuántas veces se debe repetir un proceso.
