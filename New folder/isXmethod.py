while True:
    print("Enter your age")
    age=input()
    if age.isdecimal():
        break
    print("Please Enter a number for your age")
while True:
    print("Select a new password(Letters and numbers only)")
    password=input()
    if password.isalnum():
        break
    print("Password can only have letters and numbers")
