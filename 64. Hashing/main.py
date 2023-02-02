import hashlib, binascii, os
 
def encrypt_string(str): # basic hashing (not good for passwords)
    sha_signature = hashlib.sha256(str.encode()).hexdigest()
    return sha_signature

print(encrypt_string("password"))
print(encrypt_string("password"))

def hash_password(password): # hash the string
    # salt basically puts text in the beginning/middle/end of the string to make strings differ from each other
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii') # generate random salt
    print("salt", salt) # tutorial: so you can see the salt (remove print function for security)
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000) 
    # the above hashes the password in utf-8 (so any characters can be added to the password (emojis/japanese))
    print("pwdhash:", pwdhash) # again, don't print out the pwdhash irl (only for tutorial sake)
    pwdhash = binascii.hexlify(pwdhash) # convert bytest to string without losing data
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password): # verify string (not unhash (cant unhash))
    salt = stored_password[:64] # salt is always 64 characters long (provided at begining of string)
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000) # basically hashes the provided password
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password # compares the 2

print()
pwd1 = hash_password("password")
pwd2 = hash_password("password")
print(f"{pwd1}\n{pwd2}")
print(verify_password(pwd1, "password"))
print(verify_password(pwd2, "password"))
print(verify_password(pwd2, "notpassword"))