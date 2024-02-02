def login():
    userid = int(input("What is your user ID number? "))
    username = input("\nEnter your username: ").upper()
    password = input("\nPlease enter your password: ").upper()
    attempts = 3
    loop = True
    file = open ("credentials.txt", "r")
    line = file.readline(userid)
    while loop == True:
        
        if username + " " + password in line == line.split (',') [0] == username and line.split (',') [1] == password:
            print("Access granted.")
            loop = False
        else:
            attempts -=1
            print("\nIncorrect Credentials. Please try again.\n\nYou now have "+str(attempts) +" more attempts\n")
        username = input("\nEnter your username: ").upper()
        password = input("\nPlease enter your password: ").upper()
        if attempts < 2:
            print("\nYou have entered the Incorrect Credentials\n\nRan out of attempts")
            file.close()
            exit()
    file.close()

login()