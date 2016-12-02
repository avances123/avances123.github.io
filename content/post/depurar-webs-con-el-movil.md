+++
author = "Fabio Rueda"
date = "2016-12-01T11:32:31+01:00"
title = "Como depurar webs con el movil"
tags = ['debug','chrome','android','web']
keywords =  ['debug','chrome','android','web']
description = "Como utilizar las chrome dev tools para enchufar tu movil y ver las webs"
+++


## Viendo la web que estas haciendo directamente en tu movil
Como ya sabreis, el chrome (y quiza otros navegadores) pueden poner su viewport como el de un movil
para hacernos mas facil depurar la responsividad de nuestra web y poder ir viendo todo tipo de tamaño y forma
de pantallas.

Eso esta muy bien porque es rapidisimo, y podemos depurar como siempre con nuestro f12, aun asi, si queremos 
visualizarla desde nuestro movil, con su chrome nativo de android y tal, podemos.  Es lo que vamos a hacer hoy.

La gracia, ademas de poder ver en un movil real tu aplicacion, es que la puedes depurar en el chrome de tu pc,
con tu pantalla grande, tu raton y teclado, y eso siempre es un puntazo.

## Montando el todo en tu pc
Pues como casi siempre lo voy a montar yo en mi pc y a la vez ire escribiendo aqui, para calentar os comento que 
google tiene [una web](https://developers.google.com/web/tools/chrome-devtools/remote-debugging/) 
para hacer especificamente esto, asi que si quereis os podeis ir alli.

### Preparando el pc con Arch linux
Necesitamos el SDK de android, siempre es bueno tenerlo instalado si tienes un movil android.

```
$ yaourt android-tools android-sdk
.... instalamos.... 
$ adb version
```

Si funciona este ultimo comando podemos seguir.

### Preparando el movil
Si usas ```adb``` o algun comando con de las android tools desde tu movil ya lo tendras activado, si no, 
aqui te dejo un video de como hacerlo


{{< youtube PA135Z23sek >}}


### devtools
Una vez enchufado el movil ya solo falta configurar nuestro chrome en el pc para que descubra nuestro movil.
Abrimos las devtools con f12 y clickamos esta opcion.


![elegir device](https://developers.google.com/web/tools/chrome-devtools/remote-debugging/imgs/open-inspect-devices.png)

Una vez emparejado ya esta le lio montao, podremos ir a cualquier url que pongamos en nuestras devtools y se visitara en el movil,
depurando la web, e incluso capturando la pantalla de lo que se ve en el movil y viendolo en nuestro pantallon de developa con 
nuestro teclado y raton.

## Conclusion
Para hacer una progressive web app siempre podemos usar solo el pc e ir viendo los tamaños de la pantalla mientras desarrollamos, pero 
llegado el momento, esta funcionalidad de chrome se hace vital, para estar bien seguros de que en moviles (al menos en el tuyo propio),
la app va a funcionar correctamente. Es gratis y solo necesitas un cable usb que lo tienes ya, rata. Asi que a depurar en el movil nativamente!
