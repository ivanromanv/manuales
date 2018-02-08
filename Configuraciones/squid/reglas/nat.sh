setsebool -P squid_use_tproxy 1

echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -A INPUT -m state --state NEW -m tcp -p tcp \
     -i eth1 --dport 3128 -j ACCEPT

iptables -t nat -A PREROUTING -i eth1 -p tcp \
    --dport 80 -j REDIRECT --to-port 3128

service iptables save
