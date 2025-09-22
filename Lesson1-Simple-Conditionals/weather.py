# Unit 2 Lesson 1 Homework: Weather Advisory System
# Name: Justin P
# Date: 9/21/25

print("Weather Advisory System")
print("=" * 23)

# Step 1: Get weather information from user
# TODO: Get temperature as integer
temp = int(input("Temperature in Fahrenheit: "))

# TODO: Get sunny status and convert to boolean
sunny_input = input("Is it sunny? ")
is_sunny = sunny_input[0] == "y" or "Y"

# Step 2: Display weather report
print(f"\nWeather Report:")
# TODO: Show temperature and sunny status
print("-" * 18)
print(f"It is {temp} degrees out today!")
if is_sunny:
    print("It is sunny outside!")
else:
    print("It is cloudy outside.")

# Step 3: Temperature advice
# TODO: Use if-else to give clothing advice based on temperature
if temp > 80:
    print("It's hot!")
elif temp <= 80:
    print("It's cool!")
# Step 4: Activity suggestions  
# TODO: Use if-else to suggest activities based on sunny status
if is_sunny:
    print("Play some ball!")
else:
    print("Get on Roblox!")
print("\nStay safe and have fun!")