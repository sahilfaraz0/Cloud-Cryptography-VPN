# 🏥 Cloud-Based Healthcare Cryptography & PKI Engine

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg?style=for-the-badge&logo=mysql&logoColor=white)
![OpenVPN](https://img.shields.io/badge/OpenVPN-Secure%20Tunnel-red.svg?style=for-the-badge&logo=openvpn&logoColor=white)
![OpenSSL](https://img.shields.io/badge/OpenSSL-PKI%20Infrastructure-yellow.svg?style=for-the-badge&logo=openssl&logoColor=white)
![Cryptography](https://img.shields.io/badge/Security-AES--GCM%20%7C%20ChaCha20-brightgreen.svg?style=for-the-badge)

---

## 📌 Project Overview
This project simulates a secure, cloud-hosted cryptographic infrastructure designed for a distributed healthcare network (Al-Shifa Hospital Network - ASHN). It demonstrates the practical application of advanced cryptographic techniques to secure sensitive Patient Administration Data (PAD), Patient Finance Data (PFD), and real-time Patient Medical Data (PMD) across a Virtual Private Network (VPN).

The architecture ensures **Confidentiality, Integrity, and Authentication** by combining hybrid cryptosystems, Public Key Infrastructure (PKI), and secure database hardening.

---

## 🚀 Core Features

*   🔐 **Stream & Block Ciphers:** Utilizes `ChaCha20` for low-latency, real-time medical data encryption (PMD) and `AES-GCM` for secure bulk storage of administrative and financial data (PAD/PFD).
*   📜 **Public Key Infrastructure (PKI):** Custom Certificate Authority (CA) implementation enforcing strict mutual TLS (mTLS) authentication between regional branches and the Central Data Hub.
*   🛡️ **Secure Transit (VPN):** OpenVPN implementation providing an AES-256-GCM encrypted tunnel for all data in transit.
*   🔍 **Data Integrity & Auditing:** SHA-256 hashing for tamper detection and comprehensive, automated audit logging for all encryption/decryption events.
*   ☁️ **Cloud Database Hardening:** Integration with MySQL, featuring role-based access control and encrypted payload ingestion.

---

## 📂 Project Structure

A clean, modular architecture separating infrastructure, database interactions, and cryptographic engines.

    ASHN_Cloud_Cryptography/
    │
    ├── 📁 certificates/
    ├── 📁 config/
    │   ├── audit_log.py            
    │   ├── cert_config.py          
    │   ├── cert_verifier.py        
    │   └── db_config.py            
    │
    ├── 📁 database/                   
    │   ├── fetch_pad.py            
    │   ├── fetch_pfd.py            
    │   └── fetch_pmd.py            
    │
    ├── 📁 encryption/
    │   ├── aesgcm_encrypt.py
    │   ├── chacha20_encrypt.py
    │   └── hashing.py      
    │
    ├── 📁 MySQL/
    │   ├── ASHN_DB_Tables.sql      
    │   └── Mock_Data_CSVs/         
    │
    ├── 📁 openvpn/
    │   ├── client.ovpn             
    │   └── server.ovpn             
    │
    ├── 📄 requirements.txt            
    ├── ⚙️ main.py
    └── 📖 README.md

---

## 🏗️ System Architecture & Security Case

*(Insert your exported Goal Structuring Notation (GSN) security case map here to visualize the threat model and defense strategy.)*

### 🔑 Cryptographic Strategy
1.  **Key Encapsulation Mechanism (KEM):** RSA-based public key encryption secures the exchange of session keys.
2.  **Data Encapsulation Mechanism (DEM):** Symmetric encryption (AES/ChaCha20) handles the heavy lifting of data payloads.
3.  **Provable Security:** Designed around IND-CCA (Indistinguishability under Chosen Ciphertext Attack) principles to resist adaptive threats.

---

## 📸 Implementation Showcase

*(Add your edited, batch-processed terminal and system screenshots here to demonstrate the working implementation)*

<details>
<summary><b>View Cryptographic Execution</b></summary>
<br>

*   *Screenshot 1: PKI Certificate Generation & Verification*
*   *Screenshot 2: OpenVPN Tunnel Establishment*
*   *Screenshot 3: Live Encryption/Decryption of MySQL Payloads*

</details>

---

## ⚠️ Disclaimer
This repository represents an academic proof-of-concept for applying cryptographic controls to cloud-based systems. The included `.crt` files are for demonstration purposes only. Private keys (`.key`) and local environment files have been intentionally omitted from this public repository to maintain security best practices.
