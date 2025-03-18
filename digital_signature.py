"""
基于RSA加密算法与MD5摘要算法的数字签名及验证模块
2020/11/14

"""
import base64
import os

from Cryptodome.Hash import MD5
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15


# 密钥生成器
def KEYGenerator():
    # 产生密钥
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out1 = open("private_key.pem", "wb")
    file_out1.write(private_key)
    file_out1.close()

    # 产生公钥
    public_key = key.publickey().export_key()
    file_out2 = open("public_key.pem", "wb")
    file_out2.write(public_key)
    file_out2.close()


# 签名器
def signaturer(private_key, data):
    # 获取消息的HASH值，摘要算法MD5，验证时也必须用MD5
    digest = MD5.new(data)
    # 使用私钥对HASH值进行签名
    signature = pkcs1_15.new(private_key).sign(digest)
    return signature


# 验证器
def verifier(public_key, data, signature):
    digest = MD5.new(data)
    try:
        pkcs1_15.new(public_key).verify(digest, signature)
        return "验证成功！！！"
    except:
        return "签名无效！！！"


# 封装器
def combine(file_path):
    KEYGenerator()
    private_key = ''
    if os.path.isfile("private_key.pem"):
        with open("private_key.pem", 'rb') as file:
            private_key = RSA.import_key(open("private_key.pem").read())
    else:
        return "Err 101"
    data = ''
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            data = base64.b64encode(file.read())
    else:
        return "Err 102"
    signature = signaturer(private_key, data)
    list_send = [str(data), str(signature)]

    return "==========\n".join(list_send)


if __name__ == '__main__':
    file_path = input('请输入原文件地址：')
    sign = combine(file_path)
    obj_path = input('请输入保存将要签名文件名称带地址：')
    sign_file = open(obj_path, 'wb')
    sign_file.write(sign.encode('utf-8'))
    sign_file.close()
