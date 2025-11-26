user_name=input("enter your username :")
if (user_name=="yash"):
    print("username is valid")
    password=input("enter your password :")
    if password != "yash@123":
        print("login fail")
    else:
        print("login pass")
else:
    print(" failed")