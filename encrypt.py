#Original key: 
original_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()_-+={[}]|:'<,>.?/"

# replace each character with the corresponding character in the encryption key
def encrypt(key, password):
    # convert password to list
    password_list = list(password)
    # loop through the length of the list, replacing each character with the new character from the key
    for x in range(len(password_list)):
        character = original_key.find(password_list[x])
        password_list[x] = key[character]
    # convert the new encrypted password back to a string and send it back
    new_password = "".join(password_list)
    return new_password

# opposite of encrypt, just switch the original key and the encrypt key
def decrypt(key, password):
    # convert password to list
    password_list = list(password)
    # loop through the length of the list, replacing each character with the new character from the key
    for x in range(len(password_list)):
        character = key.find(password_list[x])
        password_list[x] = original_key[character]
    # convert the new encrypted password back to a string and send it back
    new_password = "".join(password_list)
    return new_password

# insert name and encrypted password to database
def insert(key, name, password):
    encrypted_password = encrypt(key, password)

    return

# retrieve data from database and decrypt password
def retrieve(key, name):
    password = decrypt(key, password)
    return password