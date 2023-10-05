import json

import requests
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


def generate_random_string(length=16):
    return secrets.token_hex(length // 2)

def int_array_to_string(int_array):
    byte_array = bytearray()
    for i in int_array:
        byte_array.extend(i.to_bytes(4, 'big'))  # Assume big endian
    return byte_array.decode('utf-8', errors='ignore')

# Given array
int_array = [
    1193550929,
    1635214187,
    1197891916,
    1111046002
]

# Convert to string
result = int_array_to_string(int_array)


def encrypt(plaintext, iv_hex):
    key = result  # 获取密钥    !!!!!!
    iv_bytes = iv_hex # 将十六进制IV转换为字节

    # 创建AES cipher对象
    cipher = AES.new(key=key.encode('utf-8'), mode=AES.MODE_CBC, iv=iv_bytes.encode('utf-8'))

    # 将明文从字符串转换为字节，并应用PKCS7填充
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)

    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)

    # 将加密数据转换为Base64编码的字符串
    encrypted_base64 = base64.b64encode(encrypted_data).decode()

    return encrypted_base64


# 调用函数时不传递任何参数，将使用默认长度16
iv_hex = generate_random_string()

plaintext = '{"query":"操作员","cityCode":105,"industryCodes":64,"pageNum":1,"limit":15}'

encrypted_data = encrypt(plaintext, iv_hex)



params = {
    "b": encrypted_data,
    "kiv": iv_hex}
}


