a simple Python script that encodes data from **"data.txt**" file, then encrypts it using AES algorithm 

### Dependencies :

Requires "cryptography" Library 
install it using following command (in unix systems, idk how you can install python packages in windows, last time i used it was 2016) :

`pip3 install cryptography`

or :

`pip3 install -r requirements.txt`

### Heres how it works :

#### Encoder :

it uses three custom dictionaries to encode strings

it chooses the Dictionary randomly and puts a Dictionary identifier number at the beginning of the encoded string

then it encodes the encoded data with hexadecimals 
#### Encryptor :

Encryptor grabs that data that was encoded using custom dictionary and encoded to hexadecimals and Encrypts it using a random generated Key
then it outputs the Encrypted data to **"encdata.txt"**

#### Decryptor :

Decryptor extracts data from **"encdata.txt"** 
Decrypts the data using the key provided 
#### Decoder :

At first it decodes the decrypted data from hexadecimals back to normal encoded data
then it identifies which dictionary was used
decodes the data 
and outputs it to "decdata.txt"
### Notes :

currently only supports english
