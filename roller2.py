
print("Welcome to the rollercoaster!")
height = int (input("Whats your height in cm? "))

if height >= 120: 
    print("You can ride the rollercoaster!")
    age = int (input("Whats your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age >= 12 and age < 18: 
        bill = 7
        print("The price is $7.")
    elif age >= 18 and age < 45: 
        bill = 12
        print("Adult tickets are $12.")
    elif age >= 45 and age < 55: 
        bill = 0
        print("Since youre depressed this is for free!")

    print("Want photos? Y or N")
    pic = input()

    if pic == "Y": 
        cuenta = bill + 3
        print("Your final bill is: " + str(cuenta))
    else:
        cuenta = bill
        print("Your final bill is: " + str(cuenta))
else: 
    print("You cannot ride")