from scapy.all import Ether, Raw, sendp

CHAT_ETHERTYPE = 0x88B5
INTERFACE = "Ethernet" 

DESTINATION_MAC = "B4:2E:99:BA:CE:EF"  # THis is the physical address for PC B

print("Ethernet Chat Sender Started")
print(f"Sending on interface: {INTERFACE}")
print(f"Destination MAC: {DESTINATION_MAC}")
print("Type a message and press Enter.")
print("Type 'quit' to exit.\n")

while True:
    message = input("Message: ")

    if message.lower() == "quit":
        print("Exiting sender.")
        break

    frame = (
        Ether(dst=DESTINATION_MAC, type=CHAT_ETHERTYPE)
        / Raw(load=message.encode())
    )

    sendp(frame, iface=INTERFACE, verbose=False)
    print("Message sent.")
