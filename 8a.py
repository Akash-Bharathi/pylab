#8(a) Build a network port scanner program that scans a given IP addresses to detect open ports on remote machine

import socket
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(1)
            if client_socket.connect_ex((target_ip, port)) == 0:
                print(f"Port {port}: Open")
            client_socket.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")
# Example usage
scan_ports("192.168.1.1", 1, 1000)
