# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
       bill += 2
       print (bill)
    if extra_cheese == "Y":
        bill += 1



if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1


if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1


print("Your final bill is: $" + str(bill))