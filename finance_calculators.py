#Task 1
#Finance calculator

import math

#Present user with option of either bond or investment calculationType
#Request user to select the calcuation type they need
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("\ninvestment \t - to calculate the amount of interest you'll earn on interest")
print("bond \t\t - to calculate the amount you'll have to pay on a home loan\n")
calculationType = str(input("Please enter your selection now: ").lower()) #make input lower case

#If investment selected calculate interest based on given formula
if calculationType == "investment":
	amount = float(input("Please enter the amount of money you are depositing: "))
	interestRate = float(input("Please enter the interest rate (as a percentage): "))/100.0 #convert interest to percentage
	years = int(input("Please enter the number of years you plan on investing: ")) 
	interest = str(input("Please enter the type of interest 'simple' or 'compound': ")).lower() #make input lower case
	if interest == "simple":
		futureValue = amount*(1+(interestRate*years)) #formula for simple interest
		print("\nYour future value on the invested amount will be: "+str(round(futureValue,2)))
	elif interest == "compound":
		futureValue = amount*math.pow((1+(interestRate)),years) #formula for compound interest
		print("\nYour future value on the invested amount will be: "+str(round(futureValue,2)))
	else:
		print("\nSilly billy!, please only choose either 'simple' or 'compound'") #Message to print if wrong option selected

#If bond selected calculate repayment based on given formula	
elif calculationType == "bond":
	presentValue = float(input("Please enter the present value of the house: "))
	interest = float(input("Please enter the interest rate (as a percentage): "))/100.0 #convert interest to percentage
	months = int(input("Please enter the number of months you plan on repaying the bond: "))
	repayment = (interest*presentValue)/(1-math.pow((1+interest),-months)) #formula for bond repayment
	print("\nThe repayment on your "+calculationType+" is R"+str(round(repayment,2)))

#Message to print if wrong option selected
else:
	print("\nSilly billy!, please only choose either 'investment' or 'bond'")
