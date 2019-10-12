def login():
    print ("Hello user! Please sign with your username and password!")
    username = input ("Username:")
    password = input ("Password:")

    if len(username) > 4 and len(username) <= 10 and username.isalpha() and len(password) >= 4 and len(password) <= 10 and password.isnumeric():

        print ("Hello " + username + "! Thank you for joining us!")

    else:
        print ("Please follow the rules for signing in!")
        login()    
login()

print ("Please follow the upcoming introductions!")

