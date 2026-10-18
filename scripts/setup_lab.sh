#!/bin/bash
# ====================================================================
# Cybersecurity Toolkit - Lab Setup & Verification Script
# ====================================================================

echo "[*] Checking system requirements for Cybersecurity Toolkit..."

# Check Python3
if command -v python3 &>/dev/null; then
    echo "[+] Python 3 is installed: $(python3 --version)"
else
    echo "[-] Python 3 NOT found. Please install it with: sudo apt install python3"
fi

# Check Git
if command -v git &>/dev/null; then
    echo "[+] Git is installed: $(git --version)"
else
    echo "[-] Git NOT found."
fi

# Set executable permissions on all Python tools
chmod +x network/port_scanner.py monitoring/sys_alert.py cryptography/hash_cracker.py
echo "[+] Set executable permissions (+x) on all toolkit modules."

echo "[*] Environment is ready to use!"
