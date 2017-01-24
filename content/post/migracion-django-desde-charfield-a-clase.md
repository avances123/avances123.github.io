+++
date = "2017-01-24T17:26:09+01:00"
title = "migracion django desde charfield a clase"
author = "Fabio Rueda"
tags = ['django','migraciones']
keywords =  ['django','migraciones','android','web']
description = "Cuando tenemos un campo choices en nuestro modelo y queremos sacarlo a una clase"
+++

## Introduccion
Pues nuestra aplicacion esta funcionando en produccion, nuestro modelo funciona muy bien y es bastante flexible, vamos afrontando bien los nuevos requisitos
y haciendo migraciones con exito, de pronto nos vamos dando cuenta que un campo simple de un modelo, que teniamos puesto como de tipo String, queremos que
tenga mas vidilla, por ejemplo guardamos el estilo de un disco como un string, pero a la larga nos damos cuenta que Estilo lo podemos generalizar en una clase
para poder saber mas datos del estilo, como el lugar donde se originó, o si es un subtipo de musica electronica y cosas asi.


## Origen
Partimos de esta base, guardamos el artista del album como una cadena, y ya tenemos muchos asi guardados.


```python
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
```

## Paso 1
Creamos el modelo nuevo de genero y lo enlazamos en un campo nuevo `genre_link` sin borrar el antiguo string.

```python
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    genre_link = models.ForeignKey('Genre', null=True)

class Genre(models.Model):
    name = models.CharField(max_length=255)
```

y creamos la migracion:

```bash
./manage.py makemigrations discography
```

## Paso 2
Ahora populamos el nuevo campo, creando los objetos nuevos desde la columna antigua, con una migracion vacia

```bash
./manage.py makemigrations --empty --name crea_genres discography
```

Y hacemos el codigo para sacar el texto del tipo, y crear los objetos nuevos.

```python
from __future__ import unicode_literals

from django.db import migrations


def create_genres(apps, schema_editor):
    Genre = apps.get_model('discography', 'Genre')
    Album = apps.get_model('discography', 'Album')
    for album in Album.objects.all():
        tipo, created = Genre.objects.get_or_create(name=album.artist)
        album.genre_link = tipo
        album.save()


def borra_genres(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_genres, borra_genres),
    ]
```

## Paso 3
En este punto ya tenemos nuestro problema solucionado, nos falta hacer limpieza y borrar la columna antigua.






