import scapy.all as scapy
from scapy_http import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
def process_sniffed_packet(packet):
    print(packet.show())
    # if packet.haslayer(http.HTTPRequest):
    #     print(type(packet))
sniff('Wi-Fi')