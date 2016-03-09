+++
title =  "Haciendo la vida facil al psql"
date = "2014-06-15"

+++

* Hace ya un tiempo que estoy usando [pgcli][2], mejora bastante el uso con autocompletado y mas cosas

## psql
Para los que usamos el cliente psql, hay ciertas "mejoras" o customizaciones que me gustaria compartir, todas (como muchas otras) se escriben en el fichero ~/.psqlrc, puedes descargar el [mio][1] si quieres!


### Distintos historicos
Al igual que el bash_history, guardaremos un historial de los comandos en un fichero, pero por defecto los guardamos en ~/.psql_history, con esta linea los separaremos por base de datos. Asi tendremos un ~/.psql_history-mydb1,~/.psql_history-mydb2 y no se mezclaran entre varias bases de datos.
```
\set HISTFILE ~/.psql_history- :DBNAME
```

#### Aumentar las lineas de historico
Almacenamos mas queries que por defecto
```
\set HISTSIZE 20000
```

#### Mejoramos el prompt
En la linea de comandos podremos ver a que base de datos y host estamos conectados:

```
\set PROMPT1 '%M %n@%/%R%#%x '
```
El resultado es:

```
[local] fabio@tests=#
```

#### Coloreamos el null
Cuando usamos pgsl, los nulos salen como una cadena vacia y no vemos nada, podremos reemplazar el null por cualquier valor que queramos:
```
\pset null '[NULL]'
```
El resultado es:
```
[local] fabio@tests=# insert into foo values (1,null) ;
INSERT 0 1
[local] fabio@tests=# select * from foo;
 id |  bar   
----+--------
  1 | [NULL]
(1 fila)

```

#### Demasiadas columnas para mi consola
Si queremos que psql nos cambie a formato extendido automaticamente cuando haya demasiadas columnas pondremos esto:
```
\x auto
```

#### Confirmar la salida
Si hemos creado tablas temporales o cosas propias de nuestra sesion, no queremos salirnos por error, para ello tendremos que pulsar ctrl+D 3 veces en lugar de una.
```
\set IGNOREEOF 3
```

El resultado es este:
```bash
[local] fabio@tests=# Use «\q» para salir de psql.
[local] fabio@tests=# Use «\q» para salir de psql.
[local] fabio@tests=# \q
```


[1]:https://raw.githubusercontent.com/avances123/dotfiles/master/postgresql/psqlrc
[2]:https://github.com/dbcli/pgcli
