# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = int(input("¿cuantos años te quedan? "))
time = years - int (age )
days = time * 365
weeks = time * 52
months = time * 12

print("You have "+ str(days)+" days, "+ str(weeks)+" weeks, and "+ str(months) +" months left.")
