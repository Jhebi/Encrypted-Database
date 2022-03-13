#encrypted database prototype before making password saver app
#since sqlite does not have a master password, you can't hide encryption key behind a locked database
#instead the master password is the encryption key itself
#if you hash the master password, you will get the encryption key
#master password jhebi
#hash.py contains the hash function
#encrypt.py allows you to insert and retrieve data from database

import hash
import encrypt

#get the master password
print("Please Enter Master password:", end = " ")
masterpass = input()
if masterpass != "jhebi":
    print("Error")
    quit()

#hash the password to get the encryption key
key = hash.hash(masterpass)

#insert to database or retrieve?
print("(1) insert \n(2) retrieve")
choice = int(input())
if choice == 1:
    print("Enter name: ", end = "")
    name = input()
    print("Enter password: ", end = "")
    password = input()
    encrypt.insert(key, name, password)
elif choice == 2:
    print("Enter name: ", end = "")
    name = input()
    encrypt.retrieve(key, name)
else:
    print("Invalid Choice")
