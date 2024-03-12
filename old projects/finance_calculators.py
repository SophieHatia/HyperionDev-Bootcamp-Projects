import math

print("Investment - to calculate the amount of interest you'll earn on your investment /n Bond - to calculate the amount you'll have to pay on a home loan")

I_or_B = input("Enter either 'INVESTMENT' or 'BOND' from the menu above to proceed:")
print(I_or_B)

"""checking if any capital form of the two options has been submitted. Starting with "bond"
   inputs from the user are then asked for and used to calculate the amount to be repaid per month
 """

if I_or_B == "bond" or I_or_B=="Bond" or I_or_B =="BOND":
    print("bond")
    HouseValue=float(input("What is the current value of the house? "))
    Rate=float(input("What is the interest rate percentage? (Enter as a Number Only) "))
    TimePeriod=float(input("How many months do you plan to repay the bond? "))
    AnnualRate=(Rate/100)/12
    RepayAmount=(AnnualRate*HouseValue)/(1-(1+AnnualRate)**(-TimePeriod))
    print("Amount to be paid back each month=",RepayAmount)

#Check if "investment" was entered (in any capital form). 
#ask the user to input  data and cast it as a float
#ask the user to input the type of interest they would like to check 
#create a second if statement for the 2 types of interest and use each formula to calculate the amount

elif I_or_B == "investment" or I_or_B=="Investment" or I_or_B=="INVESTMENT":
   deposit=float(input("How much money are you depositing? "))
   Rate=float(input("What is the interest rate percentage? (Enter as a Number Only) "))
   Years=float(input("How many years are you planning on investing? "))
   interest=input("Would you like 'SIMPLE' or 'COMPOUND' interest? ")
   if interest=="SIMPLE" or interest =="Simple" or interest=="simple":
      print("Calculating Simple Interest")
        #print(deposit,Rate,Years)
      Interest = deposit*(1+(Rate/100)*Years)
      print("Amount of Interest=",Interest)

   elif interest=="COMPOUND" or interest=="Compound" or interest=="compound":
      print("Calculating Compound Interest")
      Interest = deposit*(1 + (Rate/100))**Years
      print("Amount of Interest=",Interest)
   else:
      print("Choose either SIMPLE or COMPOUND interest")

# if neither 'investment' or 'bond' were entered an error message is printed asking the user to chose one of the two options
else:
    print("please choose an option from the menu above")

