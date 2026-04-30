import os

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CA_CERT     = os.path.join(BASE_DIR, "certificates", "ca.crt")
SERVER_CERT = os.path.join(BASE_DIR, "certificates", "server.crt")
SERVER_KEY  = os.path.join(BASE_DIR, "certificates", "server.key")
CLIENT_CERT = os.path.join(BASE_DIR, "certificates", "client.crt")
CLIENT_KEY  = os.pth.join(BASE_DIR, "certificates", "client.key")