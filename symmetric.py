from cryptography.fernet import Fernet

def get_key():
    return Fernet.generate_key()


def encode_text(symmetric_key: str, text: str):
    bytes_text = bytes(text, 'utf-8')
    f = Fernet(symmetric_key)
    token = f.encrypt(bytes_text)
    return token


def decode_text(symmetric_key: str, token: str):
    bytes_token = bytes(token, 'utf-8')
    f = Fernet(symmetric_key)
    decoded = f.decrypt(bytes_token)
    return decoded
