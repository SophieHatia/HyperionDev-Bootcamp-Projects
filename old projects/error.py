
print("Welcome to the error program") #Added in missing parentheses
print("\n") #Added missing parentheses and un-indented 

"""Variables declaring the user's age, casting the str to an int, and printing the result"""
age_Str = "24" #unindented and removed second = in order to define age_Str and removed the letters so string can e converted to an integer
age = int(age_Str) 
print("I'm", age, "years old.") #cannot concatenate integers and strings so changed + to ,

""" Variables declaring additional years and printing the total years of age"""
years_from_now = "3"
FutureYears = int(years_from_now) #defining years_from_now as an integer
total_years = age + FutureYears #making sure that the integer is added to the addition

print ("The total number of years:", total_years) #added missing parentheses and made sure to print total_years not the string answer:years and made sure not to concatenate int and string

"""Variable to calculate the total amount of months from the total amount of years and printing the result"""
total_months = total_years * 12 #correcting undefined "total" to "total_years" 
print ("In 3 years and 6 months, I'll be ", total_months + 6 , " months old") #changing the + to , as cannot concatenate ints and strings and added 6 to make the sentence correct
