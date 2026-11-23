
# AI & Technology Project

project_name = "AI & Technology"
learning = "Artificial Intelligence"
goal = "Solving real-world problems"

print("===== MY PROJECT =====")
print("Project:", project_name)
print("Currently Learning:", learning)
print("My Goal:", goal)

print("\n===== WELCOME =====")

name = input("Enter your name: ").strip()

if name:
    print("Hello,", name)
    print("Welcome to my learning journey!")
else:
    print("Hello, Student!")

print("\n===== AGE CHECK =====")

age_input = input("Enter your age: ").strip()

if age_input.isdigit():
    age = int(age_input)

    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")
else:
    print("Please enter a valid age.")

print("\n===== MY LEARNING GOALS =====")

goals = [
    "Learn AI",
    "Understand Technology",
    "Build Projects",
    "Solve Problems"
]

for goal_item in goals:
    print("-", goal_item)


def welcome_message(name):
    print("\nHello,", name)
    print("Welcome to AI & Technology!")


welcome_message("Student")

print("\nProject completed!")

welcome_message("Student")
