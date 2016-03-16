+++
title =  "Tablas hash en C,Javascript y Python"
date =  "2015-10-31"
path = ""
tags = ['hash','comparativa','diccionarios','rendimiento','performance']
categories = ['PoC']
languages = ['python','C','javascript']

+++

Un amigo necesitaba hacer una [funcion hash][1] para un problema concreto, como os podeis imaginar, el problema consistia en que necesitaba buscar en un diccionario muchisimas claves, este proceso necesitaba ser lo mas rapido posible, y segun nuestro cariño a distintos lenguajes ,entre varios decidimos hacer un estudio sobre como resolver el problema usando varios: C, javascript y python, sin usar ninguna cosa rara, simplemente usando lo que el lenguaje permita hacer.

### Descripcion del problema
Tenemos un fichero de texto con miles de lineas del tipo:
```
x|y  |z |v  |w         |value
9|100|33|100|2014010100|1
9|100|33|100|2014010106|5
```
Nuestro objectivo es crear una tabla hash para poder buscar segun los campos de arriba, excepto el ultimo, que es el valor que queremos extraer. Es decir la clave de busqueda seran los valores *x,y,z,v,w* y el valor el campo *value*



### Javascript
En javascript un diccionario, es un [objeto][2], es decir llenariamos un objeto cuyas propiedades son nuestras claves, no entiendo mucho la implementacion de los objetos/diccionarios en javascript asi que cualquier comentario clarificador lo agradeceria mucho.

Creamos las claves concatenando los numeros como un string y le asignamos su valor.

```js
var csv = require("fast-csv"),
    table = {};

csv.fromPath("problema.txt", { headers: true, delimiter: '|' })
 .on("record", function(data) {
    arr.push(data);
    table[data.x + data.y + data.z + data.v + data.w] = data.value
 })
```

Y recorremos el diccionario:
```javascript
var keys = Object.keys(table);
for (var m = 0; m < keys.length; m++) {
 value = table[keys[m]];
}
```
Cabe repetir que lejos de entender la implementacion interna de los objetos en javascript, no parece que sea una tabla hash sino un array asociativo, no podemos decidir una funcion hash especifica para nuestro problema.


### Python
En python los [diccionarios][3] son tablas hash, ademas, nuestras claves no tienen por que ser tipos basicos, si lo fueran seria bastante parecido al ejemplo de javascript, excepto que son tablas hash reales,aqui esta la implementacion de tuplas como claves. Cualquier objeto puede ser una clave de un diccionario, basta con que cumpla una serie de requisitos en su definicion, debemos especificar un par de cosas:

* Como sabremos que un objeto es igual a otro, para ello usaremos el metodo eq en su clase, necesitamos saberlo para decidir cuando hay una colision

* Definiremos un metodo [hash][4] para aplicar cualquier funcion que queramos en la construccion/lectura del diccionario.

Vamos a definir nuestra clase para las claves de busqueda:
```python
class Key():
    def __init__(self,x,y,z,v,w):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.v = int(v)
        self.w = int(w)

    def __str__(self):
        return str(self.x) + str(self.y) + str(self.z) + str(self.v) + str(self.w)

    def __repr__(self):
        return str(self)

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.v == other.v and self.w == other.w

    def __hash__(self):
        """
        En esta funcion debemos devolver un entero, sera nuestra funcion hash
        """
        return hash((req.x,req.y,req.z,req.v,req.w))
```
Como podemos ver, la funcion hash, nos permite contruir nuestra tabla hash con facilidad, otros ejemplos de funciones hash para este problema:

```python
def custom(self):
  return abs(req.x * (req.y + 1) * (req.z + 1) + req.v) % 1572869

def integer(self):
  return int(str(self)) # el hash de un entero en python es el propio numero
```
Favoreciendonos del lenguaje y de este metodo hash, podemos cambiar su definicion en tiempo de ejecucion, esto nos servira para comparar muchas funciones hash de manera sencilla, pero eso sera en otro post aparte.

Leemos todas las claves

```python
def dict_scan(d):
    for key in d.keys():
        d[key]
```

### C
En C no existe la estructura diccionario dentro del lenguaje, lo tenemos que hacer nosotros, esto tiene como ventaja que tenemos un control absoluto de como se tiene que comportar, ademas del rendimiento insuperable que tiene un lenguaje compilado como C. No hace falta que igual de insuperable es el tiempo que nos cuesta implementar este problema comparado con los otros dos contendientes, digamos que tenemos tiempo infinito para hacerlo.

La creacion de la estructura de datos la tabla hash es la siguiente:

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TAMHASH 1572869

typedef struct {
  int *datos;
  int num_datos;
} datos_t;

typedef struct {
  int k[5];
  int v;
} hash_datos_t;

typedef struct
{
  hash_datos_t *datos;
  int num_datos;
  int num_max_datos;
} hash_node_t;
```
La funcion hash es totalmente como nosotros queramos

```c
inline static int hash_key(int x, int y, int z, int v, int w)
{
  return (x * y * (z + 1) + v + w) % TAMHASH;
}
```
Creamos un hash vacio

```c
hash_node_t *hash_create(void)
{
  hash_node_t *hash;
  int i;

  hash = malloc(sizeof(hash_node_t) * TAMHASH);
  for(i = 0; i < TAMHASH; i++)
  {
      hash[i].datos = malloc(sizeof(hash_datos_t) * 2);
      hash[i].num_datos = 0;
      hash[i].num_max_datos = 2;
  }

  return hash;
}
```

Lo llenamos

```c
inline static void hash_add(hash_node_t *hash, int *p, int valor)
{
  int ind;
  int i;

  ind = hash_key(p[0], p[1], p[2], p[3], p[4]);

  // comprobamos si existe
  for(i = 0; i < hash[ind].num_datos; i++)
  {
    if(hash[ind].datos[i].k[0] == p[0] &&
      hash[ind].datos[i].k[1] == p[1] &&
      hash[ind].datos[i].k[2] == p[2] &&
      hash[ind].datos[i].k[3] == p[3] &&
      hash[ind].datos[i].k[4] == p[4])
      break;
  }

  if(i == hash[ind].num_datos)
  {
    // no se ha encontrado la información
    // creamos un elemento nuevo
    if(hash[ind].num_datos == hash[ind].num_max_datos)
    {
      // si hemos llegado al máximo ampliamos
      hash[ind].num_max_datos += 4;
      hash[ind].datos = realloc(hash[ind].datos,
        sizeof(hash_datos_t) * hash[ind].num_max_datos);
    }

    //memcpy(hash[ind].datos[i].k, p, sizeof(int)*5);
    hash[ind].datos[i].k[0] = p[0];
    hash[ind].datos[i].k[1] = p[1];
    hash[ind].datos[i].k[2] = p[2];
    hash[ind].datos[i].k[3] = p[3];
    hash[ind].datos[i].k[4] = p[4];
    hash[ind].datos[i].v = valor;
    hash[ind].num_datos++;
  }
  else
  {
    // lo hemos encontrado.
    hash[ind].datos[i].v = valor;
  }
}

// Metemos cada linea en el hash con la funcion de arriba
for(linea = 0; linea < datos->num_datos; linea+=6)
{
  hash_add(hash, &datos->datos[linea], datos->datos[linea + 5]);
}
```
Y lo leemos

```c
inline static int hash_get(hash_node_t *hash, int *p)
{
  int i;
  int ind;
  int ret = -1;

  ind = hash_key(p[0], p[1], p[2], p[3], p[4]);

  // comprobamos si existe
  for(i = 0; i < hash[ind].num_datos; i++)
  {
    if(hash[ind].datos[i].k[0] == p[0] &&
      hash[ind].datos[i].k[1] == p[1] &&
      hash[ind].datos[i].k[2] == p[2] &&
      hash[ind].datos[i].k[3] == p[3] &&
      hash[ind].datos[i].k[4] == p[4])
    {
      ret = hash[ind].datos[i].v;
      break;
    }
  }

  return ret;
}

// consultando datos
for(linea = 0; linea < datos->num_datos; linea+=6)
{
  v = hash_get(hash, &datos->datos[linea]);
}
```

### Metodo de resolucion de colisiones

En el caso de C, la tabla hash esta creada con un metodo de resolucion de colisiones del tipo [Separate chaining with linked lists][5], mientras que el metodo que python usa es [Open addressing][6], En esta grafica se ve como se comportan los dos metodos segun lo llena que esta la tabla (load factor), ordenadas menores es mejor.

![Grafica collision compare](http://upload.wikimedia.org/wikipedia/commons/1/1c/Hash_table_average_insertion_time.png)


### Rendimiento

Aunque no con este codigo (modificado para la explicacion), se hicieron pruebas de los tres lenguajes, siendo vencedor C (con toda optimizacion del codigo posible), y muy cerca quedo [pypy][7] con su funcion built-in de hashear tuplas, mas de tres veces mas lento quedo el cpython 2.7, y javascript en nodejs.


[1]:http://es.wikipedia.org/wiki/Tabla_hash
[2]:http://ecma262-5.com/ELS5_HTML.htm#Section_8.6
[3]:http://hg.python.org/cpython/file/52f68c95e025/Objects/dictobject.c
[4]:https://docs.python.org/2/reference/datamodel.html#object.__hash__
[5]:http://en.wikipedia.org/wiki/Hash_table#Separate_chaining_with_linked_lists
[6]:http://en.wikipedia.org/wiki/Hash_table#Open_addressing
[7]:http://pypy.org/
