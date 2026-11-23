
print("===== USER PROFILE CREATOR =====")

# Get a valid name
while True:
    name = input("Enter your name: ").strip()

    if name:
        break
    else:
        print("Name cannot be empty. Try again.")

# Get a valid age
while True:
    age = input("Enter your age: ").strip()

    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    else:
        print("Please enter a valid positive age.")

# Get interest
while True:
    interest = input("Enter your interest: ").strip()

    if interest:
        break
    else:
        print("Interest cannot be empty. Try again.")

# Display profile
print("\n===== YOUR PROFILE =====")
print("Name:", name)
print("Age:", age)
print("Interest:", interest)

print("\nProfile created successfully!")
