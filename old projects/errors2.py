
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #defining lion as a string
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a " + animal + ". It is a " + animal_type + " and it has " + str(number_of_teeth) + " teeth." #converting number of teeth to a string so that it can be concatenated. ending each section of "" to use each variable and not use the names as strings
#swapping animal type and number of teeth so the sentence makes sense

print(full_spec) #added missing parentheses
