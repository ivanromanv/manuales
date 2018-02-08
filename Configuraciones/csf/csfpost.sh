#sh /bin/service network restart
#sh /etc/squid/reglas/fw107.sh
sh /etc/squid/reglas/fw50.sh
sh /etc/squid/reglas/fwopenvpn.sh
sh /etc/squid/reglas/fwanchobanda.sh
# enmascaramiento
#iptables -t nat -A POSTROUTING -o ens+ -j MASQUERADE
