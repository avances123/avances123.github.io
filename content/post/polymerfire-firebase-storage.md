+++
author = "Fabio Rueda"
date = "2016-10-05T18:29:06+02:00"
title = "polymerfire y firebase-storage"
tags = ['polymer','firebase','s3']
keywords = ["polymer","firebase","s3","aws","polymerfire","firebase-storage"]
description = "Usando firebase-storage para sustituir S3"
+++

# Motivacion
Como siempre empiezo con algo personal y nada tecnico, esta vez me propongo hacer una web prescindiendo totalmente de AWS, google sigue impulsando [firebase][3], asi que voy a utilizar su base de datos para mi app, como siempre la parte de permisos para la db sigue siendo lo mas engorroso y aun no he tocado bien, llegado el momento escribire otro post acerca de ese "maldito" json de configuracion.

Ya use los elementos antiguos creados por google mismo para firebase de polymer, ahora los han renovado para la nueva API de firebase y lo han llamado [polymerfire][4]. La interaccion con la base de datos sigue siendo maravillosa, pero ahora firebase tiene un sistema donde dejar blobs creados por el usuario, normalmente fotos, un S3, pero sin tener que ir a AWS y manteniendo un solo proveedor para tu backend, firebase.

# Que es firebase-storage
Pues es la competencia de google a S3 de Amazon. El servicio que presta google para almacenar ficheros en la nube, se suele usar para subir los estaticos de nuestras apps, o para que nuestros usuarios suban sus fotos, tipica feature de "upload your avatar" que tienen las apps.

El servicio como tal se llama [Cloud Storage][1] y si creas un proyecto de firebase, lo tendras a tu disposicion como [Firebase Storage][2], no deja de usar la infraestructura del primero pero ya viene perfectamente preparado para poder utilizarlo con las credenciales de tu proyecto.

Por defecto, los permisos para subir ficheros (imagen,audio,video,texto, etc.) son para usuarios autenticados en este proyecto, cosa que en polymer con firebase-auth es algo trivial. De hecho funciona tan bien que tardas en pensar en los permisos ya que todo esta perfectamente preparado a unos requisitos mas o menos normales, en los que solo los usuarios registrados pueden subir ficheros.

# Como se sube un fichero a firebase-storage con polymerfire
Pues yo no he visto la forma, no hay un elemento para eso aun, pero seguramente lo habra, en todo caso, polymerfire tiene un fichero llamado polymer-app.html que importas para inicializar el objeto firebase, objeto que es el que aparece en toda la documentacion de la libreria js de firebase y que podemos usar en nuestra app de polymer llamandolo simplemente en nuestro codigo.

Si escribimos esto en cualquier html en el que hayamos importado polymerfire/firebase-app.html, funcionara, y a partir de ahi, podemos seguir con la [documentacion oficial][5] para subir ficheros a firebase-storage


```javascript
var storageRef = firebase.storage().ref();
```

## Metadatos
Ademas puedes almacenar parejas de clave-valor (metadatos) al fichero que se esta subiendo, cosa que me ha encantado, porque puede la imagen llevar asociados datos que quiza puedan ser utiles, de momento no lo he usado pero creo que S3 no tiene algo parecido.

# Conclusion
Pues con firebase-storage parece que ahora se puede hacer una app sin pasar por AWS, yo antes guardaba las imagenes en base64 en el propio documento en la base de datos, o subia a S3, supongo que habria mas formas de hacerlo, pero sin duda ahora, este paso critico que muchas apps tendran como subir por parte de los usuarios, queda totalmente cubierto.




[1]: https://cloud.google.com/storage/
[2]: https://firebase.google.com/docs/storage/
[3]: https://firebase.google.com/
[4]: https://elements.polymer-project.org/elements/polymerfire
[5]: https://firebase.google.com/docs/storage/web/upload-files?hl=es
