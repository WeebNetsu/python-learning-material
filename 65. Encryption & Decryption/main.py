# python3 -m pip install cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key() # will generate a key... SAVE it (or write it to file with python to encrypt and decrypt in this session only)
print(key)

# with open("key.txt", "wb") as file: # open the file in write+byte mode
    # file.write(key)

with open("key.txt", "rb") as file: # get the key from file
    the_key = file.read()

print(the_key)

message = "this will be encrypted"

# encrypt
encoded_message = message.encode()
f = Fernet(the_key)
encrypted_message = f.encrypt(encoded_message)
print(encrypted_message)

# decrypt
decrypted_message = f.decrypt(encrypted_message)
decoded_message = decrypted_message.decode() # changes message from bytes object to string
print(decoded_message)