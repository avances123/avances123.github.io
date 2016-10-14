+++
author = "Fabio Rueda"
date = "2016-10-12T19:05:03+02:00"
title = "Congelar un paquete en arch linux"
tags = ['arch','pacman','postgresql']
keywords = ['arch','pacman','Arch Linux Archive']
description = "Como bajar de version un paquete y como forzar una version en Arch linux con pacman"
+++

# Introduccion
Creo que es una de las cosas que se dice muy poco de Arch Linux y que me ha hecho enamorarme mas aun de esta distribucion, se trata del downgrade de paquetes.

Mi problema ha sido este, Yo uso postgresql, para guardar datos, mapas etc, para las webs que hago en django y en general para [trastear](https://www.depesz.com/).

El postgresql almacena los datos en un formato que cambia entre versiones, asi que si tienes un postgresql 9.4 en tu ordenador funcionando, con sus bases de datos, y lo actualizas a 9.5, el nuevo no arrancará, necesitas actualizar el formato de los datos que almacenaba el 9.4.

Arch linux es una [rolling release](https://en.wikipedia.org/wiki/Rolling_release), que hablando mal es que esto no para de actualizarse sin parar,digo hablando mal (yo me incluyo,hasta no hace mucho decia lo mismo) porque no es asi para nada. Si eres usuario de arch linux conoceras el comando `pacman -Syu`, sirve para actualizar tus paquetes, es como `apt-get upgrade` en los sistemas debian. Pues si pacman detecta que hay un paquete llamado postgresql-9.5 que actualiza a tu instalado postgresql-9.4, lo cambiara y pondra el nuevo. Lo correcto es siempre saber que estas actualizando y tener un control, sobre todo en el entorno de la empresa, en nuestras casas somos mas de actualizar todo y tener el asunto bien nuevecito.

Pero claro hay ciertos paquetes que no son el `htop` y que actualizarlos no puede ser tan sencillo, es el caso de postgresql. Siguiendo con nuestro problema, en este punto hemos actualizado y tenemos un flamante postgresql-9.5 que no arranca, ya que su configuracion apunta a un directorio de datos con _formato_ de 9.4.

# Downgrade de un paquete
Hemos actualizado a postgresql-9.5 pero necesitamos volver a 9.4 para actualizar los datos, este paso se sale del proposito de este post, hay muchas formas, pero la que me gusta a mi ya que no tengo muchos datos es volcar toda la base de datos en texto a un fichero con `pg_dumpall`.

Necesitamos postgresql-9.4 para arrancar y hacer el dump, pero hemos actualizado a 9.5,[hay que volver](https://wiki.archlinux.org/index.php/Downgrading_packages), como se hace esto? pues realemente es muy sencillo y elegante.

## Arch Linux Archive
ALA es una coleccion de snapshots de los repositorios, por fecha. Es decir guarda como eran los repos de nuestros paquetes para un dia determinado.

Para pillar nuestro postgresql-94, buscamos en la carpeta [packages](https://archive.archlinux.org/packages) donde estan todos los paquetes y sus versiones. Nos lo bajamos y lo instalamos asi
```
cd /tmp/
wget https://archive.archlinux.org/packages/p/postgresql/postgresql-9.4.5-1-x86_64.pkg.tar.xz
sudo pacman -U postgresql-9.4.5-1-x86_64.pkg.tar.xz
```


# Forzar una version de un paquete y no actualizarla
Bueno ya vamos arreglando el embrollo, una vez hecho el dump a texto, volvemos a postgresql-9.5 y lo cargamos y ya tenemos nuestro postgresql nuevecito con nuestros datos. Ahora queremos que no nos vuelva a suceder en la 9.6. Vamos a forzar a quedarnos con esta version de postgresql y que pacman pase de actualizar a 9.6 aunque lo encuentre, porque cuando esto suceda, nos saldra por pantalla, haremos el dump a texto, y podremos actualizar nuestros datos.

En nuestro `/etc/pacman.conf` editamos esta linea:

```
IgnorePkg   = postgresql postgresql-libs postgis
```

Y listo, ya no nos volvera a pasar el mismo problema.


# Dejar de ser una rolling release
Gracias a ALA, nuestro mirrorlist puede estar puesto a un dia fijo, esto significara que nunca veremos actualizaciones nuevas, tendremos un sistema estable y seguro, donde conocemos todas las versiones de los paquetes y estamos conformes.

Basta con actualizar nuestros repos a ese dia en ALA, actualizando nuestro `/etc/pacman.d/mirrorlist`

```
##
## Arch Linux repository mirrorlist
## Generated on 2042-01-01
##
Server=https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
```

 El dia queramos gastar tiempo de nuestro equipo en actualizar todo el sistema operativo, tendriamos que cambiar la fecha en la url de nuestro mirror y trabajar para que la actualizacion funcione. Se acabaron las excusas para no utilizar Arch en produccion!
