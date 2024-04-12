
# Importing required libraries

import random

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

# Writing the output to "encdata.txt"

outputFile = open("encdata.txt", "w")
outputFile.write(str(finalResult))

