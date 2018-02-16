/sbin/iptables -t nat -A POSTROUTING -o p2p1 -j MASQUERADE
/sbin/iptables -A FORWARD -i p2p1 -o p4p1 -m state --state RELATED,ESTABLISHED -j ACCEPT
/sbin/iptables -A FORWARD -i p4p1 -o p2p1 -j ACCEPT

