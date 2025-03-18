from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP


class RsaGenerator(object):
    def __init__(self):
        super(RsaGenerator, self).__init__()
        # 产生密钥
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key()
        file_out1 = open("private.pem", "wb")
        file_out1.write(self.private_key)
        file_out1.close()

        # 产生公钥
        self.public_key = self.key.publickey().export_key()
        file_out2 = open("receiver.pem", "wb")
        file_out2.write(self.public_key)
        file_out2.close()


# 加密数据
def encrypt(content):
    data = content.encode("utf-8")
    file_out = open("encrypted_data.bin", "wb")
    # 载入公钥
    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)  # 产生随机16字节的aes密匙

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    file_out.close()
    return str(ciphertext)


# 解密数据
def decrypt():
    file_in = open("encrypted_data.bin", "rb")
    private = open("private.pem")
    private_key = RSA.import_key(private.read())

    enc_session_key, nonce, tag, ciphertext = \
        [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    file_in.close()
    private.close()
    return data.decode("utf-8")


if __name__ == '__main__':
    data = input('请输入数据:')
    rsa = RsaGenerator()
    print(encrypt(data))
    print(decrypt())
    print(rsa.private_key)
    rsa = RsaGenerator()
    print(encrypt(data))
    print(decrypt())
    print(rsa.private_key)
