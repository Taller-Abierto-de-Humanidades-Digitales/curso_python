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

# Diccionarios

Los diccionarios son estructuras de datos que permiten asociar información a través de claves y valores. De cierta manera, un diccionario puede ir desde algo muy simple hasta prácticamente representar una base de datos. En este capítulo veremos cómo crear diccionarios, cómo acceder a sus elementos y cómo modificarlos.

## Creando diccionarios

Los diccionarios se definen con llaves `{}` y los elementos se separan con comas `,`. Por ejemplo, un diccionario con los protagonistas de la serie de televisión "Friends" se puede definir como:

```{code-cell} ipython3
protagonistas = {
    "Rachel": "Jennifer Aniston",
    "Monica": "Courteney Cox",
    "Phoebe": "Lisa Kudrow",
    "Joey": "Matt LeBlanc",
    "Chandler": "Matthew Perry",
    "Ross": "David Schwimmer"
}

protagonistas
```

De esa manera, tenemos un listado de los protagonistas y a cada uno de ellos le hemos asignado un valor. En este caso, el valor es el nombre del actor o actriz que lo interpretó.

## Operaciones con diccionarios

Eric Matthes explica que un diccionario es "una colección de *pares de valores clave*" donde "cada *clave* está conextada a un valor, y se puede usar una clave para acceder a un valor asociado con dicha clave" {cite}`matthes_python_2016`. El valor de una clave puede ser cualquier tipo de dato, incluso otro diccionario. 

Por ejemplo, podemos hacer un diccionario más complejo para que cada protagonista tenga un diccionario con sus datos personales:

```{code-cell} ipython3
protagonistas = {
    "Rachel": {
        "nombre": "Jennifer Aniston",
        "año_nacimiento": 1969,
        "nacionalidad": "Estadounidense",
        "género": "Femenino"
    },
    "Monica": {
        "nombre": "Courteney Cox",
        "año_nacimiento": 1964,
        "nacionalidad": "Estadounidense",
        "género": "Femenino"
    },
    "Phoebe": {
        "nombre": "Lisa Kudrow",
        "año_nacimiento": 1963,
        "nacionalidad": "Estadounidense",
        "género": "Femenino"
    },
    "Joey": {
        "nombre": "Matt LeBlanc",
        "año_nacimiento": 1967,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    },
    "Chandler": {
        "nombre": "Matthew Perry",
        "año_nacimiento": 1969,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    },
    "Ross": {
        "nombre": "David Schwimmer",
        "año_nacimiento": 1966,
        "nacionalidad": "Estadounidense",
        "género": "Masculino"
    }
}

protagonistas
```

De esa manera podemos acceder no solamente a un valor asociado a una clave (por ejemplo, el nombre de la actriz que intepretó a Rachel), sino también a un diccionario asociado a una clave (por ejemplo, la edad de cada uno de los protagonistas).

### Accediendo a los elementos de un diccionario

Para acceder a los elementos de un diccionario, podemos usar la sintaxis `diccionario[clave]`. Por ejemplo, para acceder al nombre de la actriz que interpretó a Rachel:

```{code-cell} ipython3
protagonistas["Rachel"]["nombre"]
```

Presta atención a la sintaxis que usamos para acceder al valor deseado. Primero, accedemos al diccionario `protagonistas` y luego a la clave `"Rachel"`. Esa clave nos devuelve un diccionario con los datos de Rachel. Finalmente, accedemos a la clave `"nombre"` para obtener el valor deseado.

Hagámoslo por pasos:

```{code-cell} ipython3
# aquí accedemos al diccionario "protagonistas" y a la clave "Rachel"
valor1 = protagonistas["Rachel"]
print(valor1)
```

```{code-cell} ipython3
# aquí accedemos al diccionario "valor1" y a la clave "nombre"
valor2 = valor1["nombre"]
print(valor2)
```

Si la clave no existe, Python nos arrojará un error indicando que la clave es incorrecta:

```{code-cell} ipython3
protagonistas["Chandler"]["apellido"]
```

### Agregando elementos a un diccionario

Para agregar elementos a un diccionario, podemos usar la sintaxis `diccionario[clave] = valor`. Por ejemplo, para agregar el apellido de Chandler:

```{code-cell} ipython3
protagonistas["Chandler"]["apellido"] = "Bing"
protagonistas["Chandler"]
```

Notarás que el orden de los elementos no cambió. Esto es porque los diccionarios no tienen un orden definido. También notarás que no hay problema con que los demás miembros de la serie no tengan apellido. Pero si intentáramos acceder al apellido de Rachel, Python nos arrojaría un error:

```{code-cell} ipython3
protagonistas["Rachel"]["apellido"]
```

Una estrategia clave para trabajar con diccionarios es la consistencia. Modificar un diccionario para que todos los elementos tengan la misma estructura es una buena práctica, incluso si los valores de algunos elementos son nulos.

### Eliminando elementos de un diccionario

Para eliminar elementos de un diccionario, podemos usar la instrucción `del`. Por ejemplo, para eliminar el apellido de Chandler:

```{code-cell} ipython3
del protagonistas["Chandler"]["apellido"]
protagonistas["Chandler"]
```

Volvimos al diccionario original :D

### Modificar los valores de un diccionario

Para modificar los valores de un diccionario, podemos usar la sintaxis `diccionario[clave] = valor`. Por ejemplo, para modificar el nombre de la actriz que interpretó a Rachel:

```{code-cell} ipython3
protagonistas["Rachel"]["nombre"] = "Jennifer Joanna Aniston"
protagonistas["Rachel"]
```

Incluso podemos hacer una operación y devolver una nueva clave con la edad de Rachel basados en el año de nacimiento:

```{code-cell} ipython3
protagonistas["Rachel"]["edad"] = 2022 - protagonistas["Rachel"]["año_nacimiento"]
protagonistas["Rachel"]
```

## Síntesis

Ya abordamos los aspectos básicos de los diccionarios. Hasta ahora, hemos visto cómo modificar elementos individuales de las listas y de los diccionarios. Esta operación sería demasiado tardada si simplemente la hicieramos manualmente, no tendría ningún sentido. 

Como dijimos al principio, vamos desde lo más simple hasta lo más complejo. Así que ya que descubrimos cómo hacer operaciones básicas con nuestros tipos de datos, vamos a ver en la siguiente sección cómo realizar operaciones repetitivas con *loops*, cómo tomar decisiones con *condicionales* y cómo definir funciones para reutilizar código.
