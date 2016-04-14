+++
date = "2016-04-13T10:30:57+01:00"
title = "Montando un firewall con arch linux y nftables"
tags = ['arch','firewall']
keywords = ["arch","archlinux","servidor","nftables","iptables","firewall"]
description = "Como hacer firewall con nftables"
+++


# Montar un firewall con nftables para nuestro servidor
Todos conocemos iptables, al menos de oidas, de poner alguna regla normalmente copiada de algun blog como este para enrutar trafico o abrir algun puerto. En este caso vamos a hacer lo mismo, pero con nftables, que es digamos la evolucion de iptables , y tiene soporte para ipv6 y arp mejorada a la que tiene iptables, ademas de una sintaxis mas amigable.

Es necesario tener un kernel >=3.13

## Instalacion
Asi de sencillo:

```bash
$ pacman -S nftables
```

## Desactivacion de iptables
Yo estaba usando iptables con un conjunto de reglas, vamos a deshabilitarlo en el systemd y a comprobar que no tenemos ninguna regla activa:

```bash
$ systemctl stop iptables
$ systemctl disable iptables
$ iptables -nvL
Chain INPUT (policy ACCEPT 72M packets, 83G bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain FORWARD (policy ACCEPT 1639K packets, 230M bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 52M packets, 10G bytes)
 pkts bytes target     prot opt in     out     source               destination
```

Ahora tenemos nuestro servidor abierto a todo, sin ningun tipo de reglas, y asi seguira porque hemos hecho disable.

## Configuracion de nftables
Por supuesto no voy a competir con la estupenda documentacion de arch linux sobre [nftables][1]. Voy a empezar con el fichero de ejemplo que esta en ```/etc/nftables.conf```. En este fichero viene la tipica configuracion de te capo todo menos el ssh para que sigas configurando y no se te quede cara de pipas.

Segun abrimos el fichero no entendemos mucho, pero el caso es pensar igual que con iptables, es exactamente igual pero digamos que puedes escribir cosas en mas sitios para mejorar la organizacion, pero los conceptos son los mismos.

Estan las *rules* que son la tipica linea de iptables, donde segun el paquete que venga, si hace match , hacemos cosas (solemos aceptarlo o rechazarlo).
Estan las *chains* que son agrupaciones de rules, solo que en lugar de tenerlas mas o menos fijas, aqui podemos tener tantas como queramos llamarlas como queramos y en general, son mas flexibles, en el fichero por ejemplo tenemos tres chains que se llaman como las antiguas de iptables, pero se podrian llamar de otra manera, el caso es, cuando entrara un paquete por ella? bueno porque en la primera de una chain de nftables debes definir sus propiedades, es decir escribir una linea de este tipo:

```text
type filter hook input priority 0;
```

Esto significa que esta chain filtrara, (simplificando se dedicara a aceptar o rechazar paquetes), y se lanzara cuando tenga el hook input, es decir cuando en el destino del paquete aparezca la ip de nuestro servidor, es decir, entra en nosotros. Tambien hay hooks ```output,forward,prerouting y postrouting``` como en iptables.

## Activar al inicio
Una vez tengamos nuestras reglas puestas en ```/etc/nftables.conf``` podemos cargarlas en cada arranque.

```
$ systemctl enable nftables
```



[1]: https://wiki.archlinux.org/index.php/nftables
