# 🛡️ Applied Cryptography in the Cloud: ASHN VPN & Data Security

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![OpenVPN](https://img.shields.io/badge/OpenVPN-Secure_Tunnel-orange?style=for-the-badge&logo=openvpn)
![Cryptography](https://img.shields.io/badge/Cryptography-AES--GCM%20%7C%20ChaCha20-success?style=for-the-badge)

## 📌 Project Overview

This repository contains a comprehensive cryptographic and network security implementation developed for **PakSecure Cyber Solutions**, serving the **Al-Shifa Hospital Network (ASHN)**. 

The primary objective of this project is to apply advanced cryptographic techniques to secure a distributed healthcare data network across a cloud-based Virtual Private Network (VPN). The system ensures the confidentiality, integrity, and authenticity of highly sensitive patient records—including Patient Administration Data (PAD), Patient Medical Data (PMD), and Patient Finance Data (PFD)—both in transit and at rest.

---

## ✨ Security Architecture & Features

This project was engineered around a strict security case argument map, treating the Central Data Hub (CDH) as the primary asset. By combining IND-CCA secure key exchanges with IND-CPA secure data encapsulation mechanisms, the system mitigates Man-in-the-Middle (MITM) attacks, unauthorized data tampering, and key exposure risks.

### 🔐 Cryptographic Controls
* **Hybrid Cryptosystem for Data at Rest:**
  * **AES-GCM (Block Cipher):** Authenticated encryption utilized for highly sensitive, structured PAD and PFD storage.
  * **ChaCha20 (Stream Cipher):** Low-latency encryption applied to continuous, real-time Patient Medical Data (PMD) generated from ICU monitoring.
* **Double Encryption VPN Tunnel:** Secure transmission between regional hospital branches (e.g., Karachi) and the Central Data Hub (Islamabad) is maintained using an OpenVPN tunnel secured with AES-256-GCM.
* **Public Key Infrastructure (PKI):** Mutual TLS (mTLS) certificate exchange enforces strict, certificate-based authentication using a custom Root Certificate Authority (CA).
* **Data Integrity Verification:** SHA-256 hashing is implemented to actively detect unauthorized data modifications during the decryption phase.
* **Comprehensive Audit Logging:** Automated tracking and logging of all system operations, including certificate verification, encryption, and decryption events.

---

## 📂 Repository Organization

The project is modularized for clarity and maintainability:

* **`/certificates/`** - Contains the Root CA, Server, and Client keys/certificates required for PKI authentication.
* **`/config/`** - Manages database connections, certificate routing, and the audit logging engine.
* **`/database/`** - Scripts dedicated to fetching, encrypting, and decrypting the PAD, PFD, and PMD tables.
* **`/encryption/`** - Core cryptographic logic housing the AES-GCM, ChaCha20, and SHA-256 hashing algorithms.
* **`/openvpn_setup/`** - Configuration files (`.ovpn`) necessary for establishing the secure client-server tunnel.
* **`/sql/`** - Database schemas and initialization scripts to deploy the Central Data Hub architecture.
* **`/docs/`** - Contains system execution screenshots, architectural diagrams, and project documentation.

---

## 🚀 Installation & Setup Guide

### 1. Prerequisites
Ensure you have MySQL Server installed and running on your machine. You will also need Python 3.x installed. 

Install the required Python dependencies:
```bash
pip install -r requirements.txt
