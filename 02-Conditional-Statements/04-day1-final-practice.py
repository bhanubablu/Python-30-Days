# ==========================================
# DAY 1 - FINAL COMBINED PYTHON PRACTICE
# Candidate Interview Checker
# ==========================================

# Get information from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
python_score = int(input("Enter your Python score: "))
city = input("Enter your city: ")


# Check interview eligibility
# Both conditions must be True:
# 1. Age must be 18 or above
# 2. Python score must be 70 or above

if age >= 18 and python_score >= 70:
    print(f"Hello {name}")
    print(f"City: {city}")
    print("You are eligible for the interview.")
else:
    print(f"Hello {name}")
    print(f"City: {city}")
    print("You are not eligible for the interview.")