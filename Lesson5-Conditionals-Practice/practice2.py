# Question2
score = int(input("Enter your score: "))
if score >= 5000:
    print("New high score!")
else:
    print("Keep trying!")

# Question 4 
height = int(input("Enter height in inches: "))
age = int(input("Enter your age: "))
if height >= 65 and age >= 14:
    print("Welcome to the team!")
else:
    print("Sorry, requirements not met.")

# Question 6
day_of_week = input("Enter day of week: ")
days_of_week = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
length = len(days_of_week)
for i in days_of_week:
    if days_of_week[i] not in day_of_week:
        print("Invalid day.")
if day_of_week[0,2] == days_of_week[5] or days_of_week[6]:
    print("Sleep in!")
else:
    print("Time to wake up!")

# Question 8:
age = int(input("Enter your age: "))
if age < 5 or age > 65:
    print("Free ticket!")
elif 5 <= age <= 17:
    print("Ticket price: $12") 
else:
    print("Ticket price: $15")

# Question 10
class_choice = input("Choose class: ")
strength = int(input("Enter strength (1-20): "))
if class_choice == "warrior" and strength > 15:
    print("Mighty warrior!") 
elif class_choice == "warrior" and strength <= 15:
    print("Training needed.")
else:
    print("Different path chosen.")

# Question 12
views = int(input("Enter view count: "))
status = "viral" if views > 10000 else ("trending" if views > 1000 else "growing")
print(f"Video status: {status}")