from scapy.all import *
from scapy.all import TCP, IP

packet = rdpcap('./gmail.pcapng.cap')
print(packet)
p = packet[0]
p.show()
data = packet[3]
data.show()

# Create an IP/TCP packet
packet = IP() / TCP()

# Display the details of the packet
packet.show()