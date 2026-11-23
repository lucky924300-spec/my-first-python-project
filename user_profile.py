print("===== USER PROFILE =====")

name = input("Enter your name: ")
while True:
    age = input("Enter your age: ")

    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a valid number.")
