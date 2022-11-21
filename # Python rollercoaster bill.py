# Python rollercoaster bill

print("Hello & Welcome to Python Rollercoaster")
height = int(input("You have to be above 150cm to ride, what is your height: "))


ticket = 0

if height > 150:
    print("Great you meet the height requirement!")
    age = int(input("What is your age? : ")) 
    if age < 12:
        ticket += 5
        print("Your ticket will cost $5")
    elif age <= 18:
        ticket += 10
        print("Your ticket will cost $10")
    elif age > 40 and age < 50:
        ticket += 0
        print("Your ticket is on the house!")
    elif age > 18:
        ticket += 20
        print("Your ticket will cost $20")
else:
    print("You do not meet the height requirements for the ride")

image = input("Would you like images, Y or N: ")
if image == "Y":
    ticket += 3
    print("Images will cost $3")
else:
    print("No additional charge for images")



print(f"Your ticket comes to ${ticket}")