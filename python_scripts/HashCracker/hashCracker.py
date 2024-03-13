# -------------------------------------------------------------------------------
# Name:        BURN
# Purpose:     SHA / MD5 hash dictionary cracker. BURN takes the hashed input
# 		   from the file passed to it and guesses the type of hashs in the file.
#		   Then it attempts a dictionary attack against the hashed strings by hashing
#		   known passwords from the dictionary file given to it at runtime
#		   and encoding some of the characters in the file with commonly used #		#   	   	   characters to double the size of the dictionary file.
#		   Note: The file format for the hash file is one hash per line. BURN will #	#		   attempt to crack each hash it finds in the file.
#
#		   Example: An entry of admin in the dictionary file will prompt BURN to also
#		   try using @dm!n.
#
# Author:      David Probert
#
# Created:     August 15 2012
# Copyright:   (c)DavidProbert2012
# Licence:     Free
# -------------------------------------------------------------------------------
# !/usr/bin/env python

import hashlib, sys

if len(sys.argv) < 3:
    sys.exit("\nUsage: " + sys.argv[0] + " <file containing hashes> <dictionary file>\n")

dic = {'a': '@', 'e': '3', 'i': '!', 'l': '1', 's': '$'}


def replace_all(text, dic):
    for a, b in dic.items():
        text = text.replace(a, b)
    return text


hashfile = sys.argv[1]
passwordfile = sys.argv[2]

hsh = open(hashfile, 'r')
hshty = hsh.readlines()
htype = ""
n = ""

for enc in hshty:
    n = enc.strip()
    lc = len(n)
    if str(lc) == "32":
        htype = "md5"
    if str(lc) == "40":
        htype = "sha1"
    if str(lc) == "56":
        htype = "sha224"
    if str(lc) == "64":
        htype = "sha256"
    if str(lc) == "96":
        htype = "sha384"
    if str(lc) == "128":
        htype = "sha512"

    hashlst = open(passwordfile, 'r')
    hashes = hashlst.readlines()
    for hash in hashes:
        x = hash.strip()
        l = replace_all(x, dic)
        bts = bytes(x, 'utf-8')
        btsenc = bytes(l, 'utf-8')
        s = getattr(hashlib, htype)
        hashval = s(bts).hexdigest()
        hashvalenc = s(btsenc).hexdigest()
        if hashval == n:
            print("\n" + htype + " Password found for hash " + n + "! The password is " + hash)
        if hashvalenc == n:
            print(htype + " Password found for hash " + n + "! The password is " + l)