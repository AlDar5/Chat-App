# Tis script generates a hash from a password to use it as an encryption key in
# symmetric encryption.
#
# [HOW TO USE]
# - Just provide a salt (from "os.urandom(16)" to get a random salt)
# The salt is used as an extra step for security
#
# - And prompt the user for a password (here for testing purposes i use "password")
# And if this script is passed identically to the other user and inputs the correct
# password it will create the same base 64 byte string to use as a key in symmetric
# encryption
#
#
# To use it just import this script/module and call the "GENERATE_KEY" function
# providing it with a password and some salt (in byte format)




import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# password_provided = "password" # Thats the password for testing pourposes
#
# password_provided = input("Whats the password for encryption?:") # This is input in the form of a string
#
# salt_provided = b'\xe94\x86S\xa8\xfc/\nk)\xa5[\x853$\x92'


def GENERATE_KEY(XpasswordX, salt):
    password = XpasswordX.encode() # Convert to type bytes
    # salt = b'\xe94\x86S\xa8\xfc/\nk)\xa5[\x853$\x92' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

    return key


def ENCRYPT(key, message):
    # [ATTENTION] The "message" MUST already be in byte format

    f = Fernet(key)
    encrypted_message = f.encrypt(message)

    # returns the message in byte format
    return encrypted_message


def DECRYPT(key, encrypted_message):
    # [ATTENTION] The "message" MUST already be in byte format

    f = Fernet(key)
    decrypted_mesage = f.decrypt(encrypted_message)


    # returns the message in byte format
    return decrypted_mesage