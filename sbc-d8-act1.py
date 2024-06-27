def register():
    while True:
        print("Creating Account")
        username = input("Enter username > ")
        lines = [line.strip() for line in open ("username.txt")]
        if username in lines:
            print("Username Exist, Try another username!! ")
        else:
            write = open("username.txt", "a")
            print(username, file=write, end="\n") 
            write.close()
            password = input("Enter password > ")
            write = open("password.txt", "a")
            print(password, file=write, end="\n") 
            write.close()
            exit()

def login_and_changepass():
    print("Login")
    username = input("Enter username > ")
    lines = [line.strip() for line in open ("username.txt")]
    if username in lines:
        user = lines.index(username)
        lines = [line.strip() for line in open ("password.txt")]
        passwordlist = lines[user]
        while True:
            password = input("Enter password > ")
            if password == passwordlist:
                print("Log in Success!!")
                print("|||||||Welcome to you account choose what you want to do. to change pass just type 'changepass', to exit type 'ext'|||||||")  
                while True:
                    to_do = input("What do you want to do? ")
                    if to_do.capitalize() == 'Changepass':
                        lines = [line.strip() for line in open ("password.txt")]
                        currentpass = input("Enter current password > ")
                        while True:
                            if currentpass == passwordlist:
                                newpass = input("Enter new password > ")
                                lines[user] = newpass
                                write = open("password.txt", "w")
                                for i in lines:
                                    print(i, file=write, end="\n") 
                                write.close()
                                exit()


                            else:
                                print("That is not you current password !!")
                                exit()
                    elif to_do.capitalize() == 'Exit':
                        exit()
                    else:
                        print("What!!")


            else:
                print("Wrong password!! Try again")
    else:
        print("Username do not exist")


while True:
    print("""
Option              Keyword

Register account    'Register'  
                
Login account       'login'

Exit                'exit'

""")
    
    user = input("Enter keyword > ")
    if user.lower() == "register":
        register()

    elif user.lower() == "login":
        login_and_changepass()

    elif user.lower() == "exit":
        exit()

    else:
        print("Wrong keyword!!")
    
