import subprocess
import datetime

print(f"=== Raport Automat de Securitate : {datetime.datetime.now()} ===\n")

# 1. Rulez comanda 'uptime' din linux prin Python 
rezultat_uptime = subprocess.run(["uptime", "-p"], capture_output=True, text=True)
print(f"[*] Stare sistem : {rezultat_uptime.stdout.strip()}")

# 2. Verific utilizatorii conectati in acest moment ('who')
rezultat_who = subprocess.run(["who"], capture_output=True, text=True)
utilizatori = rezultat_who.stdout.strip().split("\n")
print(f"[*] Utilizatori conectati ({len(utilizatori)}):")
for u in utilizatori: 
    if u:
        print(f"    -> {u}")

# 3. Verificam porturile de ascultare locale cu 'ss'
print("\n[*] Verificare automata socket-uri deschise:")
rezultat_ss = subprocess.run(["ss", "-tuln"], capture_output=True, text=True)

if ":22" in rezultat_ss.stdout:
    print("   [!] Atentie : serviciul SSH (port 22) este activ pe aceasta masina.")
if ":80" in rezultat_ss.stdout or ":8080" in rezultat_ss.stdout:
    print("   [!] Atentie : Servicii WEB necriptate (port 80/8080) sunt expuse.")

print("\n=== Scanare de securitate finalizata ===")
