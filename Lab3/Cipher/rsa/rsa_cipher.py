import rsa, os

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    """docstring for ClassName."""
    def __init__(self):
        pass

    # gen_key(pub, pri) (1024, 2048,..)
    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    # rsa_en => pub
    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('ascii'), key)

    # rsa_de -> pri
    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    # tao chu ky so => plain, key_pri, sha-256
    def sign(self, message, key):
        return rsa.sign(message.encode('ascii'), key, 'SHA-256')

    # chung thuc => plain, chu ky so, key_pub, sha-256
    def verify(self, message, signature, key):
        try:
            return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-256'
        except:
            return False