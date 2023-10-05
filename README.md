# 字符数组到字符串转换工具

本工具提供了一种简便的方法，将整数数组转换为字符串。在处理二进制数据或与特定字符编码/解码方案交互时，这种转换可能非常有用。以下是此工具的基本使用方法和代码示例。

## 使用方法

1. **安装必要的依赖库**

在Python环境中，确保已安装了以下库:

```bash
pip install pycryptodome requests
```

2. **导入必要的库**

```python
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
```

3. **定义转换函数**

```python
def int_array_to_string(int_array):
    byte_array = bytearray()
    for i in int_array:
        byte_array.extend(i.to_bytes(4, 'big'))  # Assume big endian
    return byte_array.decode('utf-8', errors='ignore')
```

4. **使用转换函数**

```python
# Given array
int_array = [
    1193550929,
    1635214187,
    1197891916,
    1111046002
]

# Convert to string
result = int_array_to_string(int_array)
```

5. **加密示例**

```python
def encrypt(plaintext, iv_hex):
    key = result  # 获取密钥
    iv_bytes = iv_hex  # 将十六进制IV转换为字节

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
```

6. **发送请求示例**

```python
params = {
    "b": encrypted_data,
    "kiv": iv_hex
}
```

## 解释

- `int_array_to_string` 函数接受一个整数数组，并将每个整数转换为4字节的序列（假设大端字节顺序）。然后，尝试将字节数组解码为一个UTF-8字符串。
- `encrypt` 函数接受明文和一个初始化向量（IV）作为参数，并使用从整数数组转换得到的密钥执行AES加密。加密后的数据被转换为Base64编码的字符串，并返回。

## 注意

- 在解码字节数组时，可能会遇到无法解码的字节。在这种情况下，`decode`方法的`errors='ignore'`参数会导致这些字节被忽略。这可能会导致生成的字符串与预期不符。
- 此示例为简化说明而提供。在实际应用中，你可能需要考虑更多的错误处理和验证逻辑，以确保转换和加密过程的正确性和安全性。