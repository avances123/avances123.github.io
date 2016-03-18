+++
date = "2016-03-09T17:30:57+01:00"
title = "Montando un servidor casero con Arch Linux I"
tags = ['arch','servidor']

+++

## Antecedentes
Bueno pues yo tenia en mi casa una raspberry pi, para hacer de media center y algun servicio de red mas, la tipica raspberry con un disco duro enchufado por usb.

Todo iba genial como muchos que la teneis en casa sabreis, mis pegas eran totalmente menores, que era ARM y que era ubuntu, llevo 1 año ahora que me he cambiado a Archlinux como sistema operativo principal y aunque he usado ubuntu durante años, queria cambiarme a arch linux, por supuesto muchisimo de lo que contare aqui funciona en [Archlinux ARM][1], para vuestras raspberrys, odroids y demas.

[1]:https://archlinuxarm.org/

## Un servidor hp en casa
Por la indicacion de un compañero del que siempre confio en cuanto a compras de tecnologia, me comento que habia un servidor casero muy barato, realmente son 200 euros, (4 veces mas que la pi), pero realmente era la posibilidad de tener un servidor *empresarial* en casa. Es el [HP Proliant Microserver gen8][2], supongo que han sacado otra version mas nueva y esta aun la venden en amazon, pero por ese precio me parecio muy barato. Gasta mas que la pi, pero no tengo que tener el disco duro enchufao ahi con cables por usb 2.0 y asi podria seguir justificandome un rato mas, en general digamos que es un salto mas, en potencia y en gasto como es normal.

El servidor esta muy bien, tiene una bios muy pro, no hace nada de ruido y diria que hasta es bonito, tiene dos tarjetas de red, y otra dedicada para su gestion remota.


[2]:http://www8.hp.com/es/es/products/proliant-servers/product-detail.html?oid=5379860#!tab=specs


## Montando los discos
Bueno como muchos de vosotros, yo tengo en mi casa varios discos cada uno de su padre y de su madre, uno que he robado de un pc viejo, otro que me he comprado, otro que me lo dio mi hermano, etc. Esta maquina tiene cuatro bahias para discos duros

![](/images/proliant_1.jpg)

Justo tenia 4 asi que los 4 para dentro, son de tamaño distintos y aunque este servidor tiene controladora RAID, yo los pinche y luego en el Arch ya los gestionaria. No se pueden pinchar en caliente, asi que hay que hacerlo con el servidor apagado, y una cosa que tiene tener un servidor mas empresarial, es que tardan en arrancar la vida, asi que pensaroslo bien!.


## Montando el SO
Para el sistema operativo, correria en un usb para no tener el sistema en ninguno de mis cuatro discos, y dedicarlos a hacer mantener los datos, sin tener el sistema entre ellos *molestando*. Para montar un arch linux en un usb, seria del genero tonto documentar cosas que estan en la estupendisima [wiki][3]. Pero bueno en general lo interesante de este paso es saber que el sistema esta en un usb, el usb tiene una escritura reducida asi que hay que minimizarla al maximo, en mi caso sacaria la particion ```/var``` y la ```/home``` a los discos de las bahias, y asi tendria el pincho usb sin casi escritura.

Sobre la configuracion del sistema operativo pues hablare constantemente en esta serie, pero sobre la [instalacion desde cero][4] de arch, no voy a poner nada ya que creo que no aporta nada de valor.

### kernel
Una cosa importante en este paso, instalar el kernel lts, que tiene menos actualizaciones, y bloquearlo, no queremos que nuestro servidor este cambiando de kernel tan tranquilamente, funciona y no hace falta actualizarlo, recordad que buscamos la estabilidad aqui.

```bash
$ sudo pacman -S linux-lts
```

```
# /etc/pacman.conf

...
IgnorePkg = linux-lts linux-lts-headers
...
```

Con esto conseguimos tener dos kernels en nuestro grub, el paquete linux, con el kernel actualizandose a menudo , y el paquete linux-lts, que es un kernel mas estable y ademas bloqueado, lo actualiaremos cuando **necesitemos**.Este sera nuestro kernel por defecto en el arranque.



[3]:https://wiki.archlinux.org/index.php/Installing_Arch_Linux_on_a_USB_key
[4]:https://wiki.archlinux.org/index.php/Installation_guide
