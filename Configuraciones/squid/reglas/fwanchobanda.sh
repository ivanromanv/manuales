#!/bin/bash
#
#http://www.monografias.com/trabajos17/ancho-de-banda/ancho-de-banda.shtml
#
# Manual de explicacion
#https://koalasoft.wordpress.com/manuales/distribucion-del-ancho-de-banda-utilizando-htb-e-iptables/
#
#Definimos la placa de red interna, ya que es la que nos interesa administrar.
DEV="ens33"

#Definimos el camino al comando "tc", en caso de que no este en el PATH
TC="tc" 

# este es el caso en el que esta en el PATH

#Definimos las redes y subredes que vamos a restringir por categorias
MATRIZ_WIFI="192.168.50.0/24"
MATRIZ_LAN="192.168.107.0/24"
BALAO="192.168.108.0/24"
PASAJE="192.168.109.0/24"
FONOS_IP="192.168.106.0/25"

#Definimos puerto del proxy squid
PROXY="3128"

#Definimos todos los limites de ancho de banda a utilizar en Kbps.
RATE1="102400"
RATE2="2048"
RATE3="384"
RATE4="384"
RATE5="512"

# Esta linea elimina toda posible definicon anterior de FILTROS y CLASES
$TC qdisc del dev $DEV root 2>&1 >/dev/null

#Definimos las CLASES existentes, ademas de la CLASE root y la CLASE master 
#que son necesarias para el funcionamiento del script, pero que no debemos modificar.
#CLASE root y master
$TC qdisc add dev $DEV root handle 1: htb default 60
$TC class add dev $DEV parent 1: classid 1:1 htb rate ${RATE1}kbit

#CLASES y orden prioridad
#ClASE I - GERENCIA - LAN 107
$TC class add dev $DEV parent 1:1 classid 1:10 htb rate ${RATE1}kbit ceil ${RATE1}kbit prio 1
$TC qdisc add dev $DEV parent 1:10 handle 10: sfq perturb 10

#ClASE II - INTERNET - LAN 107
$TC class add dev $DEV parent 1:1 classid 1:20 htb rate ${RATE2}kbit ceil ${RATE2}kbit prio 2
$TC qdisc add dev $DEV parent 1:20 handle 20: sfq perturb 10

#ClASE III - OFICINA WIFI - LAN 50
$TC class add dev $DEV parent 1:1 classid 1:30 htb rate ${RATE3}kbit ceil ${RATE3}kbit prio 3
$TC qdisc add dev $DEV parent 1:30 handle 30: sfq perturb 10

#ClASE IV - BALAO - LAN 108
$TC class add dev $DEV parent 1:1 classid 1:40 htb rate ${RATE4}kbit ceil ${RATE4}kbit prio 4
$TC qdisc add dev $DEV parent 1:40 handle 40: sfq perturb 10

#ClASE V - PASAJE - LAN 109
$TC class add dev $DEV parent 1:1 classid 1:50 htb rate ${RATE4}kbit ceil ${RATE4}kbit prio 5
$TC qdisc add dev $DEV parent 1:50 handle 50: sfq perturb 10

#ClASE VI - FONOS_IP HCDAS - LAN 106
$TC class add dev $DEV parent 1:1 classid 1:60 htb rate ${RATE5}kbit ceil ${RATE5}kbit prio 6
$TC qdisc add dev $DEV parent 1:60 handle 60: sfq perturb 10

#Ya están las 6 CLASES definidas, ahora hay que definir los FILTROS.

# FILTRO1 (Subnet GERENCIA a CLASE I)
$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip dst $MATRIZ_LAN flowid 1:10
#$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip src $MATRIZ_LAN flowid 1:10
echo Segmento de red $MATRIZ_LAN

# FILTRO2 (INTERNET a CLASE II)
$TC filter add dev $DEV parent 1: protocol ip prio 2 u32 match ip dport $PROXY flowid 1:20
#$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip sport $PROXY flowid 1:20

# FILTRO3 (Subnet USUARIOS WIFI a CLASE III)
$TC filter add dev $DEV parent 1: protocol ip prio 3 u32 match ip dst $MATRIZ_WIFI flowid 1:30
#$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip src $MATRIZ_WIFI flowid 1:30
echo Segmento de red $MATRIZ_WIFI

# FILTRO4 (Subnet SUCURSAL BALAO a CLASE IV)
$TC filter add dev $DEV parent 1: protocol ip prio 4 u32 match ip dst $BALAO flowid 1:40
#$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip src $BALAO flowid 1:40
echo Segmento de red $BALAO

# FILTRO5 (Subnet SUCURSAL HCM a CLASE V)
$TC filter add dev $DEV parent 1: protocol ip prio 5 u32 match ip dst $PASAJE flowid 1:50
#$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip src $PASAJE flowid 1:50
echo Segmento de red $PASAJE

# FILTRO6 (Subnet FONOS_IP HCM Y BALAO CLASE VI)
$TC filter add dev $DEV parent 1: protocol ip prio 6 u32 match ip dst $FONOS_IP flowid 1:60
#$TC filter add dev $DEV parent 1: protocol ip prio 1 u32 match ip src $FONOS_IP flowid 1:60
echo Segmento de red $FONOS_IP

#Ya esta listo para correr, si queremos podemos mostrar las clases y limites establecido (no muestra a quien pertenece cada subnet o servicio).
$TC qdisc show dev $DEV
$TC class show dev $DEV

#Fin del Script
