# 🛡️ Cybersecurity & Automation Toolkit

A modular security toolkit and learning laboratory developed for Linux environments, focusing on network reconnaissance, defensive system monitoring, and cryptographic verification using **Python 3** and **Bash**.

Designed and tested on **Ubuntu Linux** and **NVIDIA Jetson (ARM64)** systems.

---

## 📂 Project Structure

```text
cyber-security-toolkit/
├── network/
│   └── port_scanner.py     # Custom TCP socket port scanner with CLI arguments
├── monitoring/
│   └── sys_alert.py        # Automated system health & security auditing tool
├── cryptography/
│   ├── hash_cracker.py     # Dictionary-based SHA-256 hash recovery tool
│   └── wordlist.txt        # Sample target wordlist
└── scripts/
    └── setup_lab.sh        # Bash environment verification and setup script

