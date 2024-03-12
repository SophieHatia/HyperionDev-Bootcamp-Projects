UserAge=float(input("What is your age? ")) #defining user inputed age as a float to check it

"""Creating qualifications for inputed ages to meet in order to print out certain responses"""

if UserAge>=100:
    print("Sorry, you're dead.")
elif UserAge>=65:
    print("Enjoy your retirement!")
elif UserAge>=40:
    print("You're over the hill.")
elif UserAge==21:
    print("Congrats on your 21st!")
elif UserAge<=13:
    print("You qualify for the kiddie discount")
else:
    print("Age is just a number")
