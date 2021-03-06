# 1ra recomendacion

ETHERNET_LAN="ens32"
ETHERNET_INTERNET="186.101.65.29"
ETHERNET_SUBNET="10.8.0.0/24"

#iptables -t nat -A POSTROUTING -s $ETHERNET_SUBNET -o $ETHERNET_LAN -j MASQUERADE
# 2da recomendacion
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -s $ETHERNET_SUBNET -j ACCEPT
iptables -A FORWARD -j REJECT
iptables -t nat -A POSTROUTING -s $ETHERNET_SUBNET -o $ETHERNET_LAN -j MASQUERADE
iptables -t nat -A POSTROUTING -j SNAT --to-source $ETHERNET_INTERNET
