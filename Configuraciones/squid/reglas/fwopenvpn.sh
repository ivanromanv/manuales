#!/bin/sh

# A Sample OpenVPN-aware firewall.

# eth0 is connected to the internet.
# eth1 is connected to a private subnet.

# Change this subnet to correspond to your private
# ethernet subnet.  Home will use HOME_NET/24 and
# Office will use OFFICE_NET/24.

#LAN INTERNET
INTERNET="ens32"

#LAN 
LAN="ens33"

PRIVATE="10.8.0.0/24"

# Loopback address
LOOP="127.0.0.1"

# Delete old iptables rules
# and temporarily block all traffic.
#iptables -P OUTPUT DROP
#ptables -P INPUT DROP
#iptables -P FORWARD DROP
#iptables -F

# Set default policies
#iptables -P OUTPUT ACCEPT
#iptables -P INPUT DROP
#iptables -P FORWARD DROP

# Prevent external packets from using loopback addr
iptables -A INPUT -i $INTERNET -s $LOOP -j DROP
iptables -A FORWARD -i $INTERNET -s $LOOP -j DROP
iptables -A INPUT -i $INTERNET -d $LOOP -j DROP
iptables -A FORWARD -i $INTERNET -d $LOOP -j DROP

# Anything coming from the Internet should have a real Internet address
iptables -A FORWARD -i $INTERNET -s 192.168.0.0/16 -j DROP
iptables -A FORWARD -i $INTERNET -s 172.16.0.0/12 -j DROP
iptables -A FORWARD -i $INTERNET -s 10.0.0.0/8 -j DROP
iptables -A INPUT -i $INTERNET -s 192.168.0.0/16 -j DROP
iptables -A INPUT -i $INTERNET -s 172.16.0.0/12 -j DROP
iptables -A INPUT -i $INTERNET -s 10.0.0.0/8 -j DROP

# Block outgoing NetBios (if you have windows machines running
# on the private subnet).  This will not affect any NetBios
# traffic that flows over the VPN tunnel, but it will stop
# local windows machines from broadcasting themselves to
# the internet.
iptables -A FORWARD -p tcp --sport 137:139 -o $INTERNET -j DROP
iptables -A FORWARD -p udp --sport 137:139 -o $INTERNET -j DROP
iptables -A OUTPUT -p tcp --sport 137:139 -o $INTERNET -j DROP
iptables -A OUTPUT -p udp --sport 137:139 -o $INTERNET -j DROP

# Check source address validity on packets going out to internet
iptables -A FORWARD -s $PRIVATE -i $LAN -j DROP

# Allow local loopback
iptables -A INPUT -s $LOOP -j ACCEPT
iptables -A INPUT -d $LOOP -j ACCEPT

# Allow incoming pings (can be disabled)
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Allow services such as www and ssh (can be disabled)
iptables -A INPUT -p tcp --dport http -j ACCEPT
iptables -A INPUT -p tcp --dport ssh -j ACCEPT

# Allow incoming OpenVPN packets
# Duplicate the line below for each
# OpenVPN tunnel, changing --dport n
# to match the OpenVPN UDP port.
#
# In OpenVPN, the port number is
# controlled by the --port n option.
# If you put this option in the config
# file, you can remove the leading '--'
#
# If you taking the stateful firewall
# approach (see the OpenVPN HOWTO),
# then comment out the line below.

iptables -A INPUT -p udp --dport 1194 -j ACCEPT

# Allow packets from TUN/TAP devices.
# When OpenVPN is run in a secure mode,
# it will authenticate packets prior
# to their arriving on a tun or tap
# interface.  Therefore, it is not
# necessary to add any filters here,
# unless you want to restrict the
# type of packets which can flow over
# the tunnel.

iptables -A INPUT -i tun+ -j ACCEPT
iptables -A FORWARD -i tun+ -j ACCEPT
iptables -A INPUT -i tap+ -j ACCEPT
iptables -A FORWARD -i tap+ -j ACCEPT

# Allow packets from private subnets
iptables -A INPUT -i $LAN -j ACCEPT
iptables -A FORWARD -i $LAN -j ACCEPT

# Keep state of connections from local machine and private subnets
iptables -A OUTPUT -m state --state NEW -o $INTERNET -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state NEW -o $INTERNET -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Masquerade local subnet
iptables -t nat -A POSTROUTING -s $PRIVATE -o $INTERNET -j MASQUERADE
