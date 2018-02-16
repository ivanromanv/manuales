firewall-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o p2p1 -j MASQUERADE
firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i p4p1 -o p2p1 -j ACCEPT
firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i p2p1 -o p4p1 -m state --state RELATED,ESTABLISHED -j ACCEPT
firewall-cmd --reload
