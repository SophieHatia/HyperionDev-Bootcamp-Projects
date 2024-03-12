#define 2 variables number and NumberSum before the while loop to make sure they are accessible outside the loop
number = 0
Number_Sum = 0
Count = 0
Average = 0
while number!= -1:                                   #set the limit that the inputed number is not -1 to iterate over until that condition is met
    number = float(input("input a number "))
    Number_Sum = Number_Sum + number
    Count = Count + 1
    if number == -1:                                  #in order to exclude -1 from the final sum create a conditional statement that if number is -1 remove it from the sum
        Number_Sum = Number_Sum - number
        Count = Count - 1
        Average = Number_Sum / Count
    print("NumberSum= ", Number_Sum)
    
print("Average= ", Average)