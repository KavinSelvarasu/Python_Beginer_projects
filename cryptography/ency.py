from cryptography.fernet import Fernet as crypto


def generateKey():
    key = crypto.generate_key()
    with open('secretkey.txt', 'w') as secretkey_file:
        secretkey_file.write(key)


def loadKey():
    return open('secretkey.txt', 'r').read()


def encrypt_message(message):
    key = loadKey()
    encode_message = message.encode()
    f = crypto(key)
    encryptedmessage = f.encrypt(encode_message)
    print(encryptedmessage)


encrypt_message('hi hello...!')
