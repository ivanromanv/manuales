#!/bin/bash
## Autor: lsilva
## Licencia: GPL v2
## Fecha de creacion: 25-09-2012
## Version: 1.0

echo limpiar reglas del cortafuegos
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
echo Dejando todas las politicas en ACCEPT
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
echo Verificando reglas
iptables -nL
echo Fin del script
