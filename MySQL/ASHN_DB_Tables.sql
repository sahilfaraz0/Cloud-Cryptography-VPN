CREATE DATABASE ashn_db;
USE ashn_db;
CREATE TABLE Patient_Admin_Data (
    patient_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    cnic VARCHAR(20),
    date_of_birth TEXT,
    contact_number VARCHAR(20),
    address TEXT,
    admission_date DATE,
    admission_reason TEXT,
    emergency_admission BOOLEAN,
    medication_prior TEXT,
    medication_prescribed TEXT,
    assigned_doctor VARCHAR(100),
    hospital_branch VARCHAR(50),
    discharge_status VARCHAR(50)
);
CREATE TABLE Patient_Medical_Data (
    pmd_id INT PRIMARY KEY,
    patient_id INT,
    full_name VARCHAR(100),
    admission_date DATE,
    heart_rate INT,
    blood_pressure VARCHAR(10),
    oxygen_level DECIMAL(4,1),
    ward VARCHAR(50),
    diagnosis TEXT,
    treatment TEXT,
    medication_administered TEXT,
    icu_notes TEXT,
    attending_doctor VARCHAR(100),
    discharge_date DATE
);
CREATE TABLE Patient_Finance_Data (
    finance_id INT PRIMARY KEY,
    patient_id INT,
    billing_date DATE,
    total_amount_pkr TEXT(12),
    payment_status VARCHAR(50),
    payment_method VARCHAR(50),
    insurance_provider VARCHAR(100),
    insurance_details TEXT,
    billing_notes TEXT,
    invoice_description TEXT,
    bank_account_number VARCHAR(30),
    tax_id VARCHAR(20),
    hospital_branch VARCHAR(50)
);
CREATE TABLE Encryption_Keys (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    table_name  VARCHAR(50),
    row_id      INT,
    column_name VARCHAR(50),
    algo        VARCHAR(20),
    enc_key     TEXT,
    nonce       TEXT,
    tag         TEXT
);
CREATE TABLE Data_Hashes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    table_name  VARCHAR(50),
    row_id      INT,
    column_name VARCHAR(50),
    hash_value  TEXT
);
CREATE TABLE Audit_Log (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    timestamp   DATETIME,
    action      VARCHAR(50),
    certificate VARCHAR(100),
    table_name  VARCHAR(50),
    status      VARCHAR(20),
    patient_id  INT
);