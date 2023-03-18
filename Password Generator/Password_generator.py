import random

characters = '~`!@#$%^^*()_+=/*-+.,""1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

while True: 
    passwordChar = int(input("Enter the no of characters you want in your password : "))

    if passwordChar < 7: 
        print("Your password will not be strong. Enter the no greater than 7")


    if passwordChar >= 8:
        password = ''
        for len in range(passwordChar):
            random_char = random.choice(characters)
            password += random_char
        

    list_pass = list(password)
    random.shuffle(list_pass)
    password_generated = ''.join(list_pass)

    filename = input("Enter the file name you wnat to save : ")

    with open(filename, 'w') as create: 
        password = 'your generated password : '
        create.write(password)
        create.write(password_generated)
    print(password_generated)
