#declared three variables 
password = "12345"
user_input = ""
user_username = ""

# while loop to keep asking the user for his username and password
while user_input != password:
    user_username = input("enter any username: ")
    user_input = input("enter the password: ")
# if statement to get access if the password is correct and if its wrong the output will print wrong password and it will get back to the while loop and ask for the password again
    if user_input == password:
        print(f"Welcome to your account {user_username}")
    else:
        print("Wrong password")