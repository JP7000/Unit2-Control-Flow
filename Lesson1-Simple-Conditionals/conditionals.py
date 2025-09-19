# UNIT 2 LESSON 1: COMPARISON OPERATORS & SIMPLE CONDITIONALS - STARTER CODE
# Follow along with your teacher!

# PART 1: Comparison Operators Practice
print("--- PART 1: Comparison Operators ---")
# Try comparing numbers with all 6 operators
age = 16
grade = 85

print(f"age = 16: {age == 16}")
print(f"age != 16: {age != 16}")
print(f"age > 16: {age > 16}")
print(f"age >= 16: {age >= 16}")
print(f"age < 16: {age <= 16}")
print(f"age <= 16: {age <= 16}")

# PART 2: Simple If Statements
print("\n--- PART 2: Simple If Statements ---")
# Create a temperature checker
temperature = 75

if temperature > 80:
    print("It's a hot day!")


# PART 3: If-Else Statements  
print("\n--- PART 3: If-Else Statements ---")
# Build a pass/fail grade system
test_score = 78

if test_score > 70:
    print("You passed!")
else:
    print("You need to retake the test!")

name = ""
if len(name) > 0:
    print("Has a name!")
if name:
    print("Has a name!")