iptables -t nat -A PREROUTING -i p4p1 -p tcp --dport 80 -j DNAT --to 10.10.1.1:3128
iptables -t nat -A PREROUTING -i p2p1 -p tcp --dport 80 -j REDIRECT --to-port 3128
iptables --t nat -A POSTROUTING --out-interface p2p1 -j MASQUERADE
