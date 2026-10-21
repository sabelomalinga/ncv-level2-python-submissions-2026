from datetime import datetime, date

#mark1 = float(input("Please enter the first number"))
#mark2 = float(input("Please enter the second number"))
#mark3 = float(input("Please enter the third mark"))

#total = (mark1 + mark2 + mark3) / 3

#print("Average is:", f"{total:.2f}")



name = input("Please type your name ")
dta = int(input("Enter the year you were born"))

dyhy = date.today().year
bornYear = dyhy - dta

print (bornYear)



