# Cloud-Based Healthcare Cryptography & PKI Engine

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)
![OpenVPN](https://img.shields.io/badge/OpenVPN-Secure%20Tunnel-red.svg)
![Cryptography](https://img.shields.io/badge/Security-AES--GCM%20%7C%20ChaCha20-brightgreen.svg)

## 📌 Project Overview
This project simulates a secure, cloud-hosted cryptographic infrastructure designed for a distributed healthcare network (Al-Shifa Hospital Network - ASHN). It demonstrates the practical application of advanced cryptographic techniques to secure sensitive Patient Administration Data (PAD), Patient Finance Data (PFD), and real-time Patient Medical Data (PMD) across a Virtual Private Network (VPN).

The architecture ensures **Confidentiality, Integrity, and Authentication** by combining hybrid cryptosystems, Public Key Infrastructure (PKI), and secure database hardening.

## 🚀 Core Features
*   **Stream & Block Ciphers:** Utilizes `ChaCha20` for low-latency, real-time medical data encryption (PMD) and `AES-GCM` for secure bulk storage of administrative and financial data (PAD/PFD).
*   **Public Key Infrastructure (PKI):** Custom Certificate Authority (CA) implementation enforcing strict mutual TLS (mTLS) authentication between regional branches and the Central Data Hub.
*   **Secure Transit (VPN):** OpenVPN implementation providing an AES-256-GCM encrypted tunnel for all data in transit.
*   **Data Integrity & Auditing:** SHA-256 hashing for tamper detection and comprehensive, automated audit logging for all encryption/decryption events.
*   **Cloud Database Hardening:** Integration with AWS RDS / MySQL, featuring role-based access control and encrypted payload ingestion.

## 🏗️ System Architecture & Security Case
*(Insert your exported Goal Structuring Notation (GSN) security case map here to visualize the threat model and defense strategy.)*

### Cryptographic Strategy
1.  **Key Encapsulation Mechanism (KEM):** RSA-based public key encryption secures the exchange of session keys.
2.  **Data Encapsulation Mechanism (DEM):** Symmetric encryption (AES/ChaCha20) handles the heavy lifting of data payloads.
3.  **Provable Security:** Designed around IND-CCA (Indistinguishability under Chosen Ciphertext Attack) principles to resist adaptive threats.

## 📸 Implementation Showcase
*(Add your edited, batch-processed terminal and system screenshots here to demonstrate the working implementation)*

<details>
<summary><b>View Cryptographic Execution</b></summary>

*   *Screenshot 1: PKI Certificate Generation & Verification*
*   *Screenshot 2: OpenVPN Tunnel Establishment*
*   *Screenshot 3: Live Encryption/Decryption of MySQL Payloads*
</details>

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/ASHN_Cloud_Cryptography.git](https://github.com/YourUsername/ASHN_Cloud_Cryptography.git)
   cd ASHN_Cloud_Cryptography
