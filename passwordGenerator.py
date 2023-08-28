import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!&^%$#@)(!^#"

while 1:
    password_jab = int(input("what length would you like your password to be : "))
    password_count = int(input("how many passwords would you like : "))
    for x in range(0, password_count):
        password = ""
        for x in range (0, password_jab):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password: ", password)   