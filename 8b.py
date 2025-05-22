#8(b) Develop a network vulnerability scanner program that not only detects open ports but also checks for known vulnerabilities on those ports.

import socket, threading

# Example CVE database
known_vulnerabilities = {
 21: ["FTP vulnerable to anonymous login (CVE-1999-0497)"],
 22: ["Old OpenSSH version (CVE-2007-3102)"],
 23: ["Telnet unencrypted (CVE-1999-0617)"],
 80: ["Apache 2.2 DoS (CVE-2011-3192)"],
 443: ["SSL BEAST attack (CVE-2011-3389)"],
 3306: ["MySQL auth bypass (CVE-2012-2122)"]
}

open_ports = []

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        open_ports.append(port)
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP address: ")
    print(f"Scanning {target} for open ports and known vulnerabilities...")
    threads = []
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("\nOpen Ports Found:")
    for port in open_ports:
        print(f"Port {port} is open.")
        if port in known_vulnerabilities:
            for vuln in known_vulnerabilities[port]:
                print(f" ⚠️ Vulnerability: {vuln}")
        else:
            print(" No known vulnerabilities in local database.")

if __name__ == "__main__":
    main()
