def authenticate():
    #Reading the file used to store the username and password data for the users 
    users_file = open("logins.txt", "a+")

    #Start of code to register a user
    def register():
        print("Please enter your details to create an account.\n")
        username = input("Username: ")
        password = input("Password: ")
        print()
        #Code to see if the username already exists in the system
        users_file.seek(0) #Goes to the beginning of the file - linear search
        for line in users_file:
            if username in line:
                print("Sorry, this username is already taken. Please try again.")
                register() #Restarts register function so that user can enter their details again with a different username
                return
        #If the username is free the program writes the name data to the file
        users_file.write(username + " " + password + "\n")
        print("Your account has been created successfully.\nPlease login.")
        login()
        return
    #End of code to register a user

    #Start of code to login an existing user
    def login():
        print("Please enter your credentials to log in.\n")
        username = input("Username: ")
        password = input("Password: ")
        print()
        
        # check if the username and password match any pair in the file
        users_file.seek(0) #Goes to the beginning of the file - linear search
        #Code to check if the username and password is valid
        for line in users_file:
            if username + " " + password in line:
                print("User, " + username + " Authenticated!")
                return username
        print("Invalid username or password. Please try again.")
        login()
        return
    #End of code to login an existing user

    #Menu for the user to choose if they want to login or register
    loop = True
    while loop == True:
        choice = input("\nDo you want to register (R) or log in (L)? ")
        if choice.upper() == "R":
            loop = False
            register()
        elif choice.upper() == "L":
            loop = False
            login()
        else:
            print("Invalid choice. Please enter R or L.")


    #Closes the file
    users_file.close()

authenticate()
print("""
---------------------------------------------
Welcome to BrindleNet!""")