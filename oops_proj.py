class chatbook:
    def __init__(self):
        self.username = ''
        self.password= ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to chatbook !! how would you like to proceed?"
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit""")
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.msg_frnd()    
        else:
            exit()

    def signup(self):
        email = input("enter your email: ")
        pwd = input("setup your password")
        self.username = email
        self.password = pwd
        print("Signup successful!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password== '':
            print("Please signup first by pressing  1 in the main menu")
        else:
            uname = input("Enter your email here")
            pwd = input("Enter your password here")
            if self.username == uname and self.password == pwd:
                print("you have a signed in successfully")
                self.loggedin = True
            else:
                print("Invalid credetnials, please try input the correct credentials")
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin == True:
            txt = input ("Enter your post here:")
            print(f"your post is now live on chatbook: {txt}")
        else:
            print("Pleae sign in first to post anything on chatbook")
            print("\n")
            self.menu()
    
    def msg_frnd(self):
        if self.loggedin == True:
            txt = input("Enter your message here:")
            frnd =input("Enter your friend's name here:")
            print(f"your message has been sent to {frnd}")
        else:
            print("please sign in first to send a message to your friend")
            print("\n")
            self.menu()


#obj = chatbook()