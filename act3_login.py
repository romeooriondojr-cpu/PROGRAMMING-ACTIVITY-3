user_name = input("Please enter your username: ")
password = input("Please enter your password: ")

stored_user = "kenzyrhon"
stored_pass = "anojay?"

if user_name == stored_user and password == stored_pass:
    print("Access granted")
else:
    print("Access denied"