#!/bin/bash
# Direccion IP del SQUID
IPSQUID=192.168.107.100

# Puerto de escucha del SQUID
PUERTOSQUID=3128

# Redireccion del Puerto 80 en TCP al puerto 3128 del SQUID.
iptables -t nat -A PREROUTING -s $IPSQUID -p tcp --dport 80 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port $PUERTOSQUID
iptables -t nat -A POSTROUTING -j MASQUERADE
iptables -t mangle -A PREROUTING -p tcp --dport $PUERTOSQUID -j DROP
