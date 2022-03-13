import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

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
    encrypted_name = encrypt(key, name)
    encrypted_password = encrypt(key, password)
    
    #check if name already exists
    cursor.execute("SELECT COUNT(*) FROM data WHERE name = ?", [encrypted_name])
    count = cursor.fetchall()
    count = count[0][0]
    if count > 0:
        print("Name already exists")
        return

    # insert name and password
    sql = "INSERT INTO data (name, pass) VALUES (?, ?)"
    values = (encrypted_name, encrypted_password)
    cursor.execute(sql, values)
    connection.commit()

    #notify that the insert is successful
    print("Data has been inserted")
    return

# retrieve data from database and decrypt password
def retrieve(key, name):
    encrypted_name = encrypt(key, name)
    # retrieve password with the corresponding name
    cursor.execute("SELECT pass FROM data WHERE name = ?", [encrypted_name])
    encrypted_password = cursor.fetchall()
    # if there are no results
    if len(encrypted_password) < 1:
        print("Results empty")
        return
    # convert the list of tuples into string
    encrypted_password = "".join(encrypted_password[0])
    password = decrypt(key, encrypted_password)

    # show the results
    print("Name: %s" % name)
    print("Password: %s" % password)
    return 