from scapy.all import sniff, Raw

CHAT_ETHERTYPE = 0x88B5
INTERFACE = "Ethernet"  
def handle_frame(frame):
    if frame.haslayer(Raw):
        message = frame[Raw].load.decode(errors="ignore")

        print("\n--- New Ethernet Chat Message ---")
        print(f"From MAC: {frame.src}")
        print(f"To MAC:   {frame.dst}")
        print(f"Message:  {message}")
        print("---------------------------------")

print("Ethernet Chat Receiver Started")
print(f"Listening on interface: {INTERFACE}")
print("Waiting for messages...\n")

sniff(
    iface=INTERFACE,
    filter="ether proto 0x88B5",
    prn=handle_frame,
    store=False
)
