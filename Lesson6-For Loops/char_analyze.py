text = input("Enter text: ")
#Count vowels
#vowel_count = 0
#vowels = "aeiouAEIOU"
#unique = ""
#for char in text:
    #if char not in unique:
        #unique += "char"
        #vowel_count += 1
#print(f"Vowel: {unique}")
#print(f"Vowels found: {vowel_count}")
capitals = ""
for char in text:
    if char not in capitals and char in "AEIOU":
        capitals += char
if capitals:
    print(f"Capital letters: {capitals}")
else:
    print("No capitals found!")
