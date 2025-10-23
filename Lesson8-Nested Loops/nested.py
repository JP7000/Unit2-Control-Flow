for row in range(3):
    for col in range(3):
        print("Hi!", end= " ")
print()

for row in range(4):
    for col in range(5):
        print("🌟", end =" ")
    print()

for row in range(3):
    for col in range(3):
        print(f"{row},{col}", end=" ")
    print()

for row in range(5):
    for col in range(row + 1):
        print(f"{row},{col}", end=" ")
    print()

for row in range(5,0,-1):
    for col in range(row):
        print("⭐️", end= "")
    print()

for row in range(1,4):
    for col in range(1,4):
        product = row * col
        print(f"{product:3}", end=" ")
    print()