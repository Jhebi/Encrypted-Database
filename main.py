#encrypted database prototype before making password saver app
#since sqlite does not have a master password, you can't hide encryption key behind a locked database
#instead the master password is the encryption key itself
#if you hash the master password, you will get the encryption key
#master password jhebi
#hash.py contains the hash function
#encrypt.py allows you to insert and retrieve data from database

import hash


