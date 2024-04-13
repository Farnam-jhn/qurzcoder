# Importing required libraries 

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode

# Extracting Encrypted data from "encdata.txt"

encrytedData = open("encdata.txt", "r")
for i in encrytedData.readlines():
    encrytedData = i

# Spliting data to indivisual pieces

devidedInput = encrytedData.split('-')
unlockKey = devidedInput[0]
data = devidedInput[1]

# Defining a funtion that decrypts the encrypted data :

def decryptData(key, ciphertext):
    key = key[:32].encode()
    ct = b64decode(ciphertext)
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message.decode()

# Decrypting the data

decrypedtData = decryptData(unlockKey, data)

# Decoding hexadecimals back to normal encoded string

encData = bytes.fromhex(decrypedtData).decode()

# Spliting data to indivisual pieces

devidedString = encData.split('-')
dictidentity = int(devidedString[0])
encodedData = str(devidedString[1])

# Recognizing which Alphabet dictionary was used

if dictidentity == 93:
    customAlphabet = {
    'a': 30, 'b': 23, 'c': 27, 'd': 11, 'e': 12, 'f': 22, 'g': 21, 'h': 29, 'i': 14, 'j': 26,
    'k': 10, 'l': 17, 'm': 24, 'n': 20, 'o': 34, 'p': 33, 'q': 18, 'r': 35, 's': 28, 't': 13,
    'u': 25, 'v': 31, 'w': 16, 'x': 32, 'y': 15, 'z': 19, ' ': 37
}
elif dictidentity == 54:
        customAlphabet = {
    'a': 22, 'b': 11, 'c': 24, 'd': 32, 'e': 29, 'f': 28, 'g': 31, 'h': 23, 'i': 19, 'j': 15,
    'k': 27, 'l': 13, 'm': 20, 'n': 14, 'o': 18, 'p': 34, 'q': 33, 'r': 21, 's': 16, 't': 10,
    'u': 25, 'v': 12, 'w': 17, 'x': 26, 'y': 35, 'z': 30, ' ': 39
}
elif dictidentity == 11:
    customAlphabet = {
    'a': 28, 'b': 35, 'c': 18, 'd': 13, 'e': 20, 'f': 17, 'g': 11, 'h': 31, 'i': 22, 'j': 21,
    'k': 16, 'l': 25, 'm': 29, 'n': 19, 'o': 34, 'p': 32, 'q': 33, 'r': 24, 's': 26, 't': 15,
    'u': 30, 'v': 12, 'w': 14, 'x': 10, 'y': 23, 'z': 27, ' ': 44
}

reversedAlphabet = {value: key for key, value in customAlphabet.items()}

# Defining a function that decodes the data

def decodeString(code, customDict):
    decoded_string = ""
    for i in range(0, len(code), 2):
        two_digit_code = code[i:i+2]
        if int(two_digit_code) in customDict:
            decoded_string += customDict[int(two_digit_code)]
        else:
            pass
    return decoded_string

finalResult = decodeString(encodedData, reversedAlphabet)

# Writing the output to "decdata.txt"

outputFile = open("decdata.txt", "w")
outputFile.write(str(finalResult))
