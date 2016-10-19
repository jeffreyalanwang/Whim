import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Variables: userName(user's name), passwordStatus(y/n: says whether the user wants a password or not),
# password(what the password is), passwordConfirm(password retyped to be confirmed),

# password_get (Get/change the password)
password = 'none1'
passwordConfirm = 'none2'


def password_get():
    global password
    password = input('Please type the password you would like: ')
    clear()
    global passwordConfirm
    passwordConfirm = input('Please retype the password: ')

# intro
print('Welcome to Whim!')
print('Failure level 0 means the message following is a warning.')
print('Failure level 1 means something went wrong, and so the process must be repeated.')
print('Failure level 2 means there was a major problem.')
print('Success means everything worked out.')
print('Type allmenu for a menu at any time in the top-level space -- this is when no programs are running.')

# setup
print('WHIM SETUP')
username = input('What is your name? ')
print('Success: Name set.')

passwordStatus = input('Would you like to use a password? y/n: ')
if passwordStatus == 'y':
    while password != passwordConfirm:
        password_get()
        if password != passwordConfirm:
            print('Failure level 1: Passwords did not match.')
        else:
            print('Success: Password set.')
input('Press enter to clear the screen and continue to the top-level space.')


# top_space
def top_space(blankscreen):
    if blankscreen == '1':
        clear()
    print('Type a command: ')

top_space('1')
