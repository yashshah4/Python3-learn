while True:
    age = str(raw_input("Enter your age : "))
    if age.isdigit():
        break
    print "Enter a number for your age"

while True:
    print "Please enter a password : "
    password = str(raw_input())
    if password.isalnum():
        break
    print "Password can only contain alphabets & numbers"
