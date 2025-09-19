height = int(input("Enter your height in inches: "))
print(f"Your height: {height} inches")
if height >= 72:
    print("Wow, you are tall!")
elif height >= 60 and height <= 71:
    print("Your height is average.")
else:
    print("Wow, you are short!")