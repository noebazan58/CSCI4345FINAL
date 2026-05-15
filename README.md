# CSCI4345FINAL
Networks project repo. Goal is to be able to communicate between 2 computers using physical ethernet and switches .
1) TO begin ensure python and scapy are installed on your machine 
   Scapy install - pip install scapy
2) On reciever pc run "ipconfig /all" get the physial address in Ethernet Adapter. Save this 
   INside sender.py input this physcial address here ---> DESTINATION_MAC
3) On reciever PC run and save show_interfaces.py, once you run it get the value of Ethernet interface. IN this case reciever PC interface is "Ethernet"
4) on Reciever pc save and run reciever.py
5) ON sender pc save and run sender.py
