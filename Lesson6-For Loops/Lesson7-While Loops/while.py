count = 5 # 1 Initialization
while count > 0: # 2 Check condition 
    print(count)
    count -= 1 # 3 update
print("Blast off!")

count = 10
while count > 0:
    print(count)
    count =- 1
text = "Bergen Tech"
length = len(text)
result = ""
i = 0
while i < length:
    if text[i].isupper():
        result += text[i]     
print(result)

#Age validator
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid! Try again.")
print(f"Your age is {age}")