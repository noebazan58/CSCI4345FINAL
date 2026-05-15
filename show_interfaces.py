from scapy.all import conf

print("Available Scapy interfaces:\n")

for iface in conf.ifaces.values():
    print("Name:", iface.name)
    print("Description:", iface.description)
    print("MAC:", iface.mac)
    print("Index:", iface.index)
    print("-" * 60)
