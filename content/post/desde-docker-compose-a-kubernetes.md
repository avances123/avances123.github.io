+++
author = 'Fabio Rueda'
date = "2020-04-11T11:32:31+01:00"
title = "Migrar una app desde docker-compose a kubernetes"
tags = ['cloud','docker','kubernetes','web','gce']
keywords =  ['cloud','docker','kubernetes','web','gce']
description = "Migrar una aplicacon que tenemos en docker-compose a la nube de google"
+++


# Desde donde partimos
Tenemos una aplicacion que consta de varios microservicios, entre ellas se comunican via http y funciona correctamente. Toda la infraesctura esta en un docker-compose.yml.
Mi plan es migrar toda la aplicacion a la nube, para asi poder tenerla disponible en cualquier sitio, aqui voy a documentar mis pasos que voy dando.

# Google Cloud

## Creamos un proyecto nuevo
Como siempre voy teniendo varias cosas entre manos me gusta tenerlo ordeando asi que en la consola de google creamos un nuevo proyecto solo para este fin.
