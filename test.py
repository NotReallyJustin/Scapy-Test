# Scapy is organized weirdly. You need scapy.all.____ for a lot of stuff. So we're just going to cut out the middleman
from scapy.all import *
import base64

# Read PCAP
PCAP_FILE = "./stomped.pcap"
packets = list(rdpcap(PCAP_FILE))

# Sort the PCAP files by time
packets_sorted = sorted(packets, key=lambda packet : packet.time)

# Loop through the packets and grab their data
b64 = b''

for packet in packets_sorted:
    # Scapy's documentation is REALLY bad
    # But there's a raw layer where you can load stuff from
    # print(packet.getlayer("Raw").load)
    b64 += packet.getlayer('Raw').load

# B64 decode
# uscg{2_m0st_p0w3rful_w4rr1ors_ar3_pati3nc3_and_t1me}
flag = base64.decodebytes(b64)
print(flag)