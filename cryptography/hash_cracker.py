import hashlib
import os
import sys

# Gasim calea absoluta a folderului in care se afla acest script
current_dir = os.path.dirname(os.path.abspath(__file__))
wordlist_file = os.path.join(current_dir, "wordlist.txt")

target_hash = "47b9cc1a4e2acecb98e1aab334b456bed1d2276291e84afd94ed9d9ed71ce02f"

print(f"[*] Incepem atacul pe baza de dictionar:")
print(f"    Hash tinta: {target_hash}")
print(f"    Wordlist:   {wordlist_file}\n")

if not os.path.exists(wordlist_file):
    print(f"[-] Eroare: Fisierul {wordlist_file} nu a fost gasit!")
    sys.exit(1)

gasit = False
with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
    for linie in f:
        cuvant = linie.strip()
        cuvant_hash = hashlib.sha256(cuvant.encode()).hexdigest()
        
        print(f"[-] Testam: {cuvant:15} -> {cuvant_hash[:16]}...")
        
        if cuvant_hash == target_hash:
            print(f"\n🎯 PAROLA A FOST SPARTA CU SUCCES: [ {cuvant} ]")
            gasit = True
            break

if not gasit:
    print("\n[!] Parola nu a fost gasita in dictionar.")
