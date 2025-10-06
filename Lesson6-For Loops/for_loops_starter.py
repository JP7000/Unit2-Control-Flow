# Lesson 5: For Loops 

# PART 1: QUICK PRACTICE - Username Loop
# =====================================
# Write a for loop to print each character in this username

username = "gamer2024"
# Your for loop here
length = len(username)
for letter in username:
    print(letter)
range(5) #0-5 (0,1,2,3,4)
range(2,5) #2-5 (2,3,4)
range(5,50,5) #5-59 (5 to 45 in increments of 5)
range(10,2,-3) #10-2 (10,8,6,4)
for i in range(len(username)):
    print(username[i])

# PART 2: CODE ALONG - Username Validator
# =====================================
# Build a username validator that checks:
# - Has at least one number
# - Has at least one uppercase letter
# - Count total characters

username = "CoolGamer123"
len = len(username)
# Your code here
char = ''
upper_checker = ""
has_number = ""
for char in username:
    if "A" <= char <= "Z":
        upper_checker = True
    if "0" <= char <= 9:
        has_number = True
print(f"Username: {username}")
print(f"Has number: {has_number}")
print(f"Length: {len}")
print(f"Is uppercase: {upper_checker}")




    

# PART 3: QUICK PRACTICE - Counting 'e'
# =====================================
# Count how many times the letter 'e' appears (case-insensitive)

tweet = "Hello everyone! Hope you're having a great day!"

e_count = 0
# Your loop here


# PART 4: CODE ALONG - Message Repeater
# =====================================
# Build a message repeater with countdown:
# - Print a message multiple times
# - Add a countdown before each message
# Example: "3... Study hard!"

message = "Study hard!"
times = 5

# Your code here


# PART 5: YOUR TURN - Text Message Analyzer
# ========================================
# - Total characters (use len())
# - Number of spaces
# - Number of letters
# - Number of punctuation marks (! ? . ,)

text = "Hey! How are you doing today? :)"

# Your analysis code here


# PART 6: PATTERN CHALLENGE
# ============================================================================

# Challenge A: Print squares of numbers 1-5 (1, 4, 9, 16, 25)


# Challenge B: Print countdown from 10 to 1


# Challenge C: Print every 3rd number from 0 to 15 (0, 3, 6, 9, 12, 15)
