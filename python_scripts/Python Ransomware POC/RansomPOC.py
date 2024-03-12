#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

# First let's find the files we want to encrypt
files = []
for file in os.listdir('/path/to/files'): # Update this to add your file path
    if os.path.isfile('/path/to/files' + file): # Update this to add your file path
        files.append(file)

def check(files):
    selection = input("Enter e to encrypt or d to decrypt.")
    if selection == 'e' or selection == 'E':
        keyCheck(files)
    elif selection == 'd' or selection == 'D':
        decFiles(files)
    else:
        exit()

def keyCheck(files):
    if os.path.isfile('encrypt.key'):
        warn = input("Warning, an encryption key already exists. If there are any encryption files on your system, continuing will erase the key needed to decrypt them. Enter C to continue or X to cancel.")
        if warn == 'x' or warn == 'X':
            exit()
        elif warn == 'c' or warn == 'C':
            encFiles(files)
        else:
            exit()
    else:
        encFiles(files)

def encFiles(files):
    # Quick function to generate a decryption key and write it to a file
    key = Fernet.generate_key()
    with open("encrypt.key", "wb") as encryptkey:
        encryptkey.write(key)

    for file in files:
        with open('/path/to/files' + file, "rb") as fileenc: # Update this to add your file path
             contents = fileenc.read()
        contents_encrypt = Fernet(key).encrypt(contents)
        with open('/path/to/files' + file, "wb") as fileenc: # Update this to add your file path
            fileenc.write(contents_encrypt)
    print("Folder contents have been encrypted.")

def decFiles(files):
    with open("encrypt.key", "rb") as key:
        secretkey = key.read()
        for file in files:
            with open('/path/to/files' + file, "rb") as filedec: # Update this to add your file path
                contents = filedec.read()
            contents_decrypt = Fernet(secretkey).decrypt(contents)
            with open('/path/to/files' + file, "wb") as filedec: # Update this to add your file path
                filedec.write(contents_decrypt)
    print("Folder contents have been decrypted.")

check(files)
