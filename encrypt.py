
# Importing required libraries

import os
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode

# Extracting data from data.txt file

data = open("data.txt", 'r')
for i in data.readlines():
    extractedData = i

# Alphabet dictionary
# Choosing which dictionary to use

randNum_0 = random.randrange(1,4)

if randNum_0 == 1 :
    customAlphabet = {
    'a': 30, 'b': 23, 'c': 27, 'd': 11, 'e': 12, 'f': 22, 'g': 21, 'h': 29, 'i': 14, 'j': 26,
    'k': 10, 'l': 17, 'm': 24, 'n': 20, 'o': 34, 'p': 33, 'q': 18, 'r': 35, 's': 28, 't': 13,
    'u': 25, 'v': 31, 'w': 16, 'x': 32, 'y': 15, 'z': 19, ' ': 37
}
    dictidentity = "93"
elif randNum_0 == 2 :
    customAlphabet = {
    'a': 22, 'b': 11, 'c': 24, 'd': 32, 'e': 29, 'f': 28, 'g': 31, 'h': 23, 'i': 19, 'j': 15,
    'k': 27, 'l': 13, 'm': 20, 'n': 14, 'o': 18, 'p': 34, 'q': 33, 'r': 21, 's': 16, 't': 10,
    'u': 25, 'v': 12, 'w': 17, 'x': 26, 'y': 35, 'z': 30, ' ': 39
}
    dictidentity = "54"
elif randNum_0 == 3 :
    customAlphabet = {
    'a': 28, 'b': 35, 'c': 18, 'd': 13, 'e': 20, 'f': 17, 'g': 11, 'h': 31, 'i': 22, 'j': 21,
    'k': 16, 'l': 25, 'm': 29, 'n': 19, 'o': 34, 'p': 32, 'q': 33, 'r': 24, 's': 26, 't': 15,
    'u': 30, 'v': 12, 'w': 14, 'x': 10, 'y': 23, 'z': 27, ' ': 44
}
    dictidentity = "11"

# Defining a functions that produces encoded data from raw data

def encodeString(string, encodingDict):
    encodedStr = ""
    for char in string:
        if char in encodingDict:
            encodedStr += str(encodingDict[char])
        else:
            pass
    return encodedStr

# Encoding the data

encodedResult = int(encodeString(extractedData, customAlphabet))
finalResult = dictidentity+"-"+str(encodedResult)

# Encoding output to hexadecimals

finalResult = finalResult.encode().hex()

# Encrypting hexadecimals to make it safe 
# Generating a random key 

cryptKey = os.urandom(32)
cryptKey = cryptKey.hex()

# Defining a fnction that encrypts finalResult

def encryptData(key, data):
    key = key[:32].encode()
    iv = b'\x00' * 16  
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(data.encode()) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_message) + encryptor.finalize()
    return b64encode(ct).decode()

# Encrypting the data

result = encryptData(cryptKey, finalResult)
result = cryptKey+"-"+result

# Writing the output to "encdata.txt"

outputFile = open("encdata.txt", "w")
outputFile.write(result)