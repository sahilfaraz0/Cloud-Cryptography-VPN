from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from config.audit_log import log_action
import datetime
import sys

def load_cert(path):
    with open(path, "rb") as f:
        return x509.load_pem_x509_certificate(f.read(), default_backend())

def verify_certificate(ca_cert_path, client_cert_path):
    print("\n" + "=" * 60)
    print("   CERTIFICATE VERIFICATION — PakSecure PKI")
    print("=" * 60)

    ca_cert     = load_cert(ca_cert_path)
    client_cert = load_cert(client_cert_path)

    # Show CA details
    print(f"\n  [CA CERTIFICATE]")
    print(f"  Issuer      : {ca_cert.subject.rfc4514_string()}")
    print(f"  Valid From  : {ca_cert.not_valid_before_utc}")
    print(f"  Valid Until : {ca_cert.not_valid_after_utc}")

    # Show client cert details
    print(f"\n  [CLIENT CERTIFICATE]")
    print(f"  Subject     : {client_cert.subject.rfc4514_string()}")
    print(f"  Issuer      : {client_cert.issuer.rfc4514_string()}")
    print(f"  Valid From  : {client_cert.not_valid_before_utc}")
    print(f"  Valid Until : {client_cert.not_valid_after_utc}")

    # Check expiry
    now = datetime.datetime.now(datetime.timezone.utc)
    if now > client_cert.not_valid_after_utc:
        print("\n  [✗] Certificate EXPIRED — Access Denied")
        sys.exit(1)

    # Verify client cert is signed by CA
    try:
        ca_public_key = ca_cert.public_key()
        ca_public_key.verify(
            client_cert.signature,
            client_cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            client_cert.signature_hash_algorithm
        )
        print("\n  [✓] Certificate valid and signed by PakSecure Root CA")
        print("  [✓] Access Granted — Decryption Authorised")
        cert_name = client_cert.subject.get_attributes_for_oid(
            x509.NameOID.COMMON_NAME)[0].value
        log_action('CERT_VERIFY', cert_name, '—', 'SUCCESS')
        return True

    except Exception as e:
        print(f"\n  [✗] Certificate verification FAILED — Access Denied")
        print(f"  Error: {e}")
        cert_name = "UNKNOWN"
        try:
            cert_name = client_cert.subject.get_attributes_for_oid(
                x509.NameOID.COMMON_NAME)[0].value
        except:
            pass
        log_action('CERT_VERIFY', cert_name, '—', 'DENIED')
        sys.exit(1)


        