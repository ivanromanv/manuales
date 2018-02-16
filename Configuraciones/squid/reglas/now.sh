iptables -t nat -A POSTROUTING -o p2p1 -j MASQUERADE
iptables -A FORWARD -i p2p1 -o p4p1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i p4p1 -o p2p1 -j ACCEPT

