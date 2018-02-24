#!/bin/bash
#
# Ethernet device name  connected to LAN
ETHERNET_LAN="p4p1"
 
# Ethernet device name connected to Internet
ETHERNET_INTERNET="p2p1"
 
# Squid Server IP Address
SQUID_SERVER_IP="10.10.1.1"
 
# Squid port number
SQUID_PORT="3128"
 
### Multiple Port Number - TCP based
MULTI_PORT="22,20,21"
 
#### Flush iptables
#iptables -F
 
##### Delete a user-defined chain
#iptables -X
 
### -t defines table ###
 
#### Flush NAT Rules/user-defined NAT chain
#iptables -t nat -F
#iptables -t nat -X
 
#### Flush Mangle Rules/user-defined NAT chain (mangle  Used for specific types of packet alteration. ) #####
#iptables -t mangle -F
#iptables -t mangle -X
 
# Load IPTABLES modules for NAT and IP conntrack
#modprobe ip_conntrack
#modprobe ip_conntrack_ftp
 
##### Enable IP forwarding for IPV4 ###
echo 1 > /proc/sys/net/ipv4/ip_forward
 
##
#Aqui
#iptables -P INPUT DROP
#iptables -P OUTPUT ACCEPT
 
#Aqui
## INPUT/OUTPUT rules for loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
 
iptables -A INPUT -i $ETHERNET_INTERNET -m state --state ESTABLISHED,RELATED -j ACCEPT
 
iptables --table nat --append POSTROUTING --out-interface $ETHERNET_INTERNET -j MASQUERADE
iptables --append FORWARD --in-interface $ETHERNET_LAN -j ACCEPT
 
iptables -A INPUT -i $ETHERNET_LAN -j ACCEPT
iptables -A OUTPUT -o $ETHERNET_LAN -j ACCEPT
 
iptables -t nat -A PREROUTING -i $ETHERNET_LAN -p tcp --dport 80 -j DNAT --to $SQUID_SERVER_IP:$SQUID_PORT
 
iptables -t nat -A PREROUTING -i $ETHERNET_INTERNET -p tcp --dport 80 -j REDIRECT --to-port $SQUID_PORT

iptables --t nat -A POSTROUTING --out-interface $ETHERNET_INTERNET -j MASQUERADE
 
#Aqui
###### IPTABLE Allow rule for tcp based multiple port
#### To disable - Use # in front of below given line
#iptables -A INPUT -p tcp -m multiport --dports $MULTI_PORT -j ACCEPT
 
#iptables -A INPUT -j LOG
#iptables -A INPUT -j DROP

#service iptables save
