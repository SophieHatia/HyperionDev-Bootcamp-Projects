#take inputs for each sport time for the user
Cycling_Time= input("Time taken to complete cycling section= ")
Running_Time = input("Time taken to complete running section= ")
Swimming_Time = input("Time taken to complete swimming section= ")

#find the totatl time of the triathlon by summing the three times, converting each input to a float from a string
Total_Time = float(Cycling_Time)+float(Running_Time)+float(Swimming_Time)
print(Total_Time)

#finding the difference in time from the minimum time for an award
Time_Diff = Total_Time - 100

#creating if statements to check the time difference to the award given for the times
if Time_Diff <= 0:
    print("You have been awarded Provincial Colours ")
elif 1<= Time_Diff and Time_Diff <= 5:
    print("You have been awarded Provincial Half Colours")
elif 6<= Time_Diff  and Time_Diff<= 10:
    print("You have been awarded Provincial Scroll")
else:
    print("You have not received an award")
