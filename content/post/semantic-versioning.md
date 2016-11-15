+++
author = "Fabio Rueda"
date = "2016-11-15T11:32:31+01:00"
title = "semantic versioning"
tags = ['bower','versiones']
keywords = ['bower','versiones','nodejs','semantic']
description = "Manera sencilla de utilizar las versiones semanticas"
+++


Desde hace ya tiempo estoy usando bower y cuando abandono un proyecto y 
lo retomo al mes o dos, se me ocurre hacer un ```bower list``` y veo que hay
paquetes que se pueden actualizar sin problema, pero ```bower update``` no me
hace caso. Abrimos el bower.json y nos encontramos con paquetes y simbolos 
y versiones.

## Versiones semanticas
Pues de esto va este post, porque estoy harto ya, y he decidido enterarme de
como van, y de paso escribir en el blog por si a alguien le interesa que se
lo expliquen como si fuera un niño de 6 años.

### Formato
Una version semantica de un paquete debe tener un formato tal que asi:
```
Major.Minor.Patch
```
Por ejemplo ```v1.3.4```

### Reglas que hay que saberse

 * Si cambia el numero del patch, es que han corregido bugs pero los cambios son
compatibles hacia atras
 * Si cambia el numero del minor, es que han añadido funcionalidades y los cambios
 siguen siendo compatibles hacia atras
 * Si cambia el numero del major, es que han metido cambios que no son compatibles 
 hacia atras
 * Otra regla mas por convenio es que si el major es 0, aun no se puede poner en
 produccion


### Los rangos (o simbolos raros) que hay que saberse
 Solo voy a poner los que no se explican por si mismos:
 * ```~1.2.0```: debe ser como minimo 1.2.0 pero nunca pasar la Minor (actualizariamos siempre pero sin llegar a 1.3)
 * ```^1.2.0```: es la que viene por defecto en npm y bower, debe ser como minimo 1.2.0 y nunca pasar la Major  (actualizariamos siempre pero sin llegar a 2.0)

Sobre esto he leido un [post interesante](https://nodesource.com/blog/semver-tilde-and-caret/)

