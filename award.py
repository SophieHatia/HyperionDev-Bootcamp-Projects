#take inputs for each sport time for the user
CyclingTime= input("Time taken to complete cycling section= ")
RunningTime = input("Time taken to complete running section= ")
SwimmingTime = input("Time taken to complete swimming section= ")

#find the totatl time of the triathlon by summing the three times, converting each input to a float from a string
TotalTime = float(CyclingTime)+float(RunningTime)+float(SwimmingTime)
print(TotalTime)

#finding the difference in time from the minimum time for an award
TimeDiff = TotalTime - 100

#creating if statements to check the time difference to the award given for the times
if TimeDiff <= 0:
    print("You have been awarded Provincial Colours ")
elif 1<= TimeDiff and TimeDiff <= 5:
    print("You have been awarded Provincial Half Colours")
elif 6<= TimeDiff  and TimeDiff<= 10:
    print("You have been awarded Provincial Scroll")
else:
    print("You have not received an award")
