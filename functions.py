import os

#todo fix the password_get
# password_get (Get/change the password)
def password_get():
    global password
    password = input('Please type the password you would like: ')
    clear()
    global passwordConfirm
    passwordConfirm = input('Please retype the password: ')


# clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
