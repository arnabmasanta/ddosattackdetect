import socket
import time
import random
import os

src_ip = "10.0.0.1"
portNum = 80
interval = 5

def generateUdpPackets():
    destIpL = { '10.0.0.2', '10.0.0.3', '10.0.0.4'}   
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    startT = time.time()
    print("Generating random packets to host on mininet simulation")
    while (time.time() - startT < interval):
        i = random.randint(2,16)
        ip = "10.0.0." + str(i)
        print(ip)
        data = os.urandom(3)
        s.sendto(data, (ip, portNum))
    s.close()

if __name__ == "__main__":
    generateUdpPackets()
