from scapy.all import *
def packet_callback(packet):
    print(packet.show())
    print("-------------------------------------------------------")

print("*******************************STARTED*********************************")
sniff(prn=packet_callback)
print ("******************************ENDING**********************************")
