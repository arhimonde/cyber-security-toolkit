import socket
import sys

# Daca utilizatorul a dat un IP ca parametru, il folosim pe acela
# Altfel, folosim localhost (127.0.0.1)
if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = "127.0.0.1"

ports_to_check = [21, 22, 80, 443, 631, 8080]

print(f"[*] Incepem scanarea pe tinta: {target}...\n")

for port in ports_to_check:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} este DESCHIS!")
    else:
        print(f"[-] Port {port} este inchis.")
        
    s.close()

print("\n[*] Scanare finalizata!")
