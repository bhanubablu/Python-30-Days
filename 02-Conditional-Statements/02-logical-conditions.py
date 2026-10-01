# 1. AND
age = int(input("Enter your age: "))
python_score = int(input("Enter your Python score: "))

if age >= 18 and python_score >= 70:
    print("You are eligible")
else:
    print("You are not eligible")


# 2. OR
has_python = True
has_java = False

if has_python or has_java:
    print("You know at least one programming language")
else:
    print("You need to learn a programming language")


# 3. NOT
is_blocked = False

if not is_blocked:
    print("User can access the website")
else:
    print("User is blocked")