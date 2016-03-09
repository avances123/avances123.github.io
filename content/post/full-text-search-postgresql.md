+++
title =  "Busquedas de texto en postgresql"
date =  "2014-11-30"

+++

# Buscando texto con postgresql

Tengo una aplicacion que usa postgresql y quiero buscar texto en ella, pero pongo *camion* sin acento y no me sale "camión", bastante tipico no?. Postgresql puede buscar entre texto como a nosotros nos gustaria, vamos a probar las funcionalidades de [full text search][1] que nos ofrece. Os adelanto que este es un ejemplo sencillisimo de todo lo que soporta.

## Tengo una columna con texto donde quiero buscar
El caso de uso mas común, tengo una tabla con texto, y al buscar puedo usar LIKE o incluso ILIKE, pero eso no nos hace encontrar las palabras como un humano quiere realmente, no vamos a lograr hacer el *quiso decir* de google, pero al menos vamos a poder buscar entre texto con o sin acentos, mayusculas, nexos y cosas asi que nos molestan.

Vamos a crear una base de datos y una tabla de prueba:
```sql
CREATE DATABASE tss;
CREATE TABLE textos (
     texto   text
);
```


Ahora insertamos texto de ejemplo:
```sql
INSERT INTO textos VALUES ('En un lugar de la Mancha');
INSERT INTO textos VALUES ('de cuyo nombre no quiero acordarme,');
INSERT INTO textos VALUES ('no ha mucho que vivía');
INSERT INTO textos VALUES ('un hidalgo de los de lanza en astillero');
INSERT INTO textos VALUES ('adarga antigua');
INSERT INTO textos VALUES ('rocín flaco y galgo corredor.');
```

Podemos buscar texto de manera precaria:
```
ts=# select * from textos where texto like 'mancha';
 texto
-------
(0 filas)

ts=# select * from textos where texto like '%mancha%';
 texto
-------
(0 filas)

ts=# select * from textos where texto ilike '%mancha%';
          texto           
--------------------------
 En un lugar de la Mancha
(1 fila)
```

Pero pronto veremos que esto no es manera, y si el usuario mete dos palabras , y si quiere buscar *rocín* sin acento? Vamos a hacerlo bien.

## Full-text search en nuestra columna
Para empezar nuestros strings deben cambiar a otro tipo llamado tsvector, que postgresql usuara para buscar de una manera eficaz, vamos nuestros strings como tsvectors:
```
ts=# select to_tsvector(texto) from textos ;
               to_tsvector                
------------------------------------------
 'lug':3 'manch':6
 'acord':6 'cuy':2 'nombr':3 'quier':5
 'viv':5
 'astiller':8 'hidalg':2 'lanz':6
 'adarg':1 'antigu':2
 'corredor':5 'flac':2 'galg':4 'rocin':1
(6 filas)
```

Muy raro todo no?, **En un lugar de la Mancha** se ha convertido en **'lug':3 'manch':6** . Un tsvector es una lista de lexemas, digamos de palabras que pueden derivar en nuestra palabra real u otras parecidas, Hemos **normalizado** nuestras palabras, es decir, las hemos puesto en minusculas, quitado los plurales, etc. Los numeros asociados, es la posicion de estas palabras en nuestro string original, En un **lug**(3) de la **manch**(6)

TODO Poner en que lenguaje esta el postgresql

## Pasarle una busqueda
Ahora que tenemos nuestros textos *arreglados* para las busquedas, podemos meter un string en la caja de busqueda, podemos meter cualquier cosa, y queremos que nos salgan los resultados razonables, para ello nuestra busqueda debemos arreglarla tambien, para ello usaremos el tipo tsquery. Este tipo, esta pensado para operar contra tsvectors como los que hemos creado antes, un ejemplo es:

```
ts=# select to_tsquery('vivir');
 to_tsquery
------------
 'viv'
(1 fila)
```

## Sacando resultados
Para buscar en nuestra tabla debemos hacer un select normal, excepto que en nuestro where usaremos el operador @@ (uno de los [muchos][2] que hay disponibles) entre nuestra tabla pasada a tsvector y nuestra busqueda pasada a tsquery

```
ts=# select * from textos where to_tsvector(texto) @@ to_tsquery('vivir');
         texto         
-----------------------
 no ha mucho que vivía
(1 fila)
```


## Ranking
Un motor de busqueda bueno, nos ordenara los resultados por relevancia, segun nos acerquemos mas a lo que queremos buscar. Postgresql tambien nos ofrece [esta funcionalidad][3], por ejemplo, si tenemos un blog, queremos que al buscar , el titulo tengas mas relevancia que el contenido, vamos a verlo:

Creamos una tabla con datos:
```sql
CREATE TABLE blog(
	titulo varchar(200),
	contenido text
);
INSERT INTO blog VALUES ('Molan las busquedas en postgresql','Estoy escribiendo un contenido del post sin la palabra maldita');
INSERT INTO blog VALUES ('Molan las busquedas en nuestra db','Estoy escribiendo un contenido del post que usa postgresql para buscar');
```

Para buscar creamos un tsvector de nuestros dos campos asi, en el ejemplo un post tiene la palabra *postgresql* en el titulo, y otro post la tiene en el contenido.
```
ts=# select to_tsvector(titulo) || to_tsvector(contenido) from blog;
                                            ?column?                                            
------------------------------------------------------------------------------------------------
 'busqued':3 'conten':9 'escrib':7 'maldit':15 'mol':1 'palabr':14 'post':11 'postgresql':5
 'busc':17 'busqued':3 'conten':10 'db':6 'escrib':8 'mol':1 'post':12 'postgresql':15 'usa':14
(2 filas)

```

Con la funcion **setweight** podemos decir que relevancia tiene un tsvector, hay pesos desde la 'D' hasta la 'A', modificamos la consulta para ponerle mas peso al titulo que al contenido:

```
ts=# select setweight(to_tsvector(titulo),'A') || setweight(to_tsvector(contenido),'B') from blog;
                                                ?column?                                                 
---------------------------------------------------------------------------------------------------------
 'busqued':3A 'conten':9B 'escrib':7B 'maldit':15B 'mol':1A 'palabr':14B 'post':11B 'postgresql':5A
 'busc':17B 'busqued':3A 'conten':10B 'db':6A 'escrib':8B 'mol':1A 'post':12B 'postgresql':15B 'usa':14B
(2 filas)
```

Ahora vemos como a los numeros de los lexemas, les ha agregado la relevancia. Ahora vamos a buscar y a ordenar los resultados, para nuestro ORDER BY usaremos la funcion ts_rank.

Nos importa mas el titulo:

```
ts=# select * from blog
where to_tsvector(titulo)||to_tsvector(contenido) @@ to_tsquery('postgresql')
order by ts_rank(setweight(to_tsvector(titulo),'D') || setweight(to_tsvector(contenido),'A'),to_tsquery('postgresql'));
              titulo               |                               contenido                                
-----------------------------------+------------------------------------------------------------------------
 Molan las busquedas en postgresql | Estoy escribiendo un contenido del post sin la palabra maldita
 Molan las busquedas en nuestra db | Estoy escribiendo un contenido del post que usa postgresql para buscar
(2 filas)
```

Nos importa mas el contenido:
```
ts=# select * from blog
where to_tsvector(titulo)||to_tsvector(contenido) @@ to_tsquery('postgresql')
order by ts_rank(setweight(to_tsvector(titulo),'A') || setweight(to_tsvector(contenido),'D'),to_tsquery('postgresql'));
              titulo               |                               contenido                                
-----------------------------------+------------------------------------------------------------------------
 Molan las busquedas en nuestra db | Estoy escribiendo un contenido del post que usa postgresql para buscar
 Molan las busquedas en postgresql | Estoy escribiendo un contenido del post sin la palabra maldita
(2 filas)
```


## Usando indices
Vaya turron de consultas las dos ultimas no?, ademas de enfarragoso, algo ineficiente, como en postgresql se pueden definir indices sobre funciones , podemos pasar lo anterior a un indice [gin][4]:

```sql
CREATE INDEX blog_posts_idx ON blog
USING gin(( setweight(to_tsvector('spanish',titulo),'B') || setweight(to_tsvector('spanish',contenido),'A')) );
```
Hemos creado un indice con la misma funcionalidad que en el anterior ejemplo, esta vez, hemos especificado a tsvector que nuestro idioma del post es español, (podriamos especificar distintos idiomas tambien). Asi nos creara el texto normalizado para nuestro idioma de manera correcta. (and o with en español no lo eliminara, seran palabras *importantes* en español).



## Mispelling
Queria buscar Quijote pero he puesto "qijote", deberia salir igual no? Para esto, tenemos [una extension][5] que podemos ponerla en nuestra db asi:
```sql
CREATE EXTENSION pg_trgm;
```
Esta extension nos da una funcion que nos da un float entre 0 y 1 llamada similarity:

```sql
ts=# select similarity('Quijote', 'Quijote');
 similarity
------------
          1
(1 fila)

ts=# select similarity('Quijote', 'Quijota');
 similarity
------------
        0.6
(1 fila)

ts=# select similarity('Quijote', 'nada que ver');
 similarity
------------
   0.105263
(1 fila)
```

Gracias a esta funcion, podremos buscar entre lexemas de nuestra tabla parecidos, pero eso sera en otro post.

### Fuentes
Me he inspirado, si no a veces copiado de este fantastico [post][6] acerca de este tema




[1]: http://www.postgresql.org/docs/9.3/static/textsearch.html
[2]: http://www.postgresql.org/docs/9.3/static/functions-textsearch.html
[3]: http://www.postgresql.org/docs/9.3/static/textsearch-controls.html#TEXTSEARCH-RANKING
[4]: http://www.postgresql.org/docs/9.3/static/textsearch-indexes.html
[5]: http://www.postgresql.org/docs/9.3/static/pgtrgm.html
[6]: http://blog.lostpropertyhq.com/postgres-full-text-search-is-good-enough/
