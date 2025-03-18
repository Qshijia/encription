import base64

from Cryptodome.PublicKey import RSA
from digital_signature import verifier

if __name__ == '__main__':
    file_path = input('请输入签名文件地址：')
    sign_file = open(file_path, 'rb')
    data_r, signature_r = list(sign_file.read().decode('utf-8').split("==========\n"))
    sign_file.close()
    data = eval(data_r)
    signature = eval(signature_r)
    public_key = RSA.import_key(open("public_key.pem").read())
    print(verifier(public_key, data, signature))
    newfile_r = base64.b64decode(data)
    obj_path = input('请输入要保存文件名称带地址：')
    newfile = open(obj_path, 'wb')
    newfile.write(newfile_r)
    newfile.close()

