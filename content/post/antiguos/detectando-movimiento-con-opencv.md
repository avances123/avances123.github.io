+++
title = "Detectando movimiento con opencv"
date = "2016-03-04"
draft = true

+++


# Detectando los movimientos de una serpiente

## Introduccion

Me he pillao una serpiente, eso es asi, es una [Thamnophis Sirtalis][1]. Lleva en su terrario 3 dias y aun esta muy asustada, el caso es que se me ocurrio una de mis frikadas con este asunto, es bastante sencilla.

Tambien me he pillado un [odroid C1][2]. Lo tendre encendido siempre, y lo uso como servidor casero, para la VPN, para el torrent, lo tipico.

## La vida de Json

Json, como se llama la culebra, esta mucho tiempo a solas, supongo que para su felicidad. El caso es que yo lo quiero mucho mas que el a mi, y lo quiero ver, asi que he montado un sistema con la [webcam][3] y el [odroid][2], que tira fotos cada minuto, y las deja un directorio, la ultima de ellas, la servire con el apache del odroid y asi tengo el terrario controlado.

Existe un programa llamado fswebcam (esta en los repos de ubuntu), que sirve precisamente para esto, tira la foto y la guarda, no hay mucho mas.

```bash
#!/bin/bash

cd /home/odroid/serpiente/
DATE=$(date +"%Y-%m-%d_%H%M")
fswebcam -v -r 800x640  -D 3 -S 4 $DATE.jpg
ln -fs $(ls -1 2015* | tail -n1) current.jpg
```

Este script es una chapuza y lo que querais, pero bueno la idea es simple, la ultima linea hace un link simbolico de la ultima foto a "current.jpg".

Este script lo ponemos en el cron del odroid para que se ejecute cada minuto.

```
* * * * * /home/odroid/timelapse-webcam.sh 2>&1 >>/tmp/timelapse.log
```

Faltaria hacer un virtualhost en nuestro apache para servir esta carpeta y currarte si quieres un html para mostrar current.jpg algo bonito.Yo solo sirvo la imagen y me sirve para verla desde el movil, podeis [verla en tiempo real][4]

## Detectando movimiento

Estos primeros dias , la culebra esta muy asustada, tiene un tronco hueco donde poderse esconder y alli pasa el 95% de su tiempo, como es rollazo estar mirando a ver que produce, he pensado en aprender algo sobre la tipico problema de detector de movimiento, hacer algo asi, y que me avise si sale del tronco o si bebe agua, esa es la idea.

Segun [he leido][5], para detectar el movimiento, usaremos la tecnica "Differential Images" que consiste en restar una imagen a otra anterior


[1]: http://es.wikipedia.org/wiki/Thamnophis_sirtalis
[2]: http://www.hardkernel.com/main/products/prdt_info.php
[3]: http://www.trust.com/en/all-products/17676-elight-full-hd-1080p-webcam
[4]: http://casa.fabio.xyz/serpiente/current.jpg
[5]: https://blog.cedric.ws/opencv-simple-motion-detection
