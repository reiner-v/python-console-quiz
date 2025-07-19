from modFiles import *

def unValidation(value):
    while True:
        if value == "":
            print("Enter a Username")
            return True
        else:
            return False

def passValidation(value):
    while True:
        if not len(value) >= 8:
            print("Enter at least 8 character ")
            return True
        elif value == "":
            print("Enter a Password")
            return True
        else:
            return False

def signIn():
    print("\t\t SIGN IN")
    print("---------------------------------")
    while True:
        username = input("Enter Username: ")
        un = unValidation(username)
        password = input("Enter Password: ")
        ps = passValidation(password)
        user = username + '-' + password + '\n'
        if not un and not ps:
            f = Files(username=username, password="", q_a="", title="", QTitles="", access="")
            un = f.signValidation(user)
            if not un:
                continue
            return un

def signUp():
    print("=================================")
    print("\t\t SIGN UP")
    print("---------------------------------")
    while True:
        username = input("Enter Username: ")
        un = unValidation(username)
        password = input("Enter Password: ")
        ps = passValidation(password)
        if not un and not ps:
            break
    createUser = Files(username, password, q_a="", title="",QTitles="",access="")
    createUser.createUsersFile()
    print("Successfully Created!")