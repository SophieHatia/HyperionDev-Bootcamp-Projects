Cycling_Time= input("Time taken to complete cycling section= ")
Running_Time = input("Time taken to complete running section= ")
Swimming_Time = input("Time taken to complete swimming section= ")

Total_Time = float(Cycling_Time)+float(Running_Time)+float(Swimming_Time)
print(Total_Time)

Time_Diff = Total_Time - 100

if Time_Diff <= 0:
    print("You have been awarded Provincial Colours ")
elif 1<= Time_Diff and Time_Diff <= 5:
    print("You have been awarded Provincial Half Colours")
elif 6<= Time_Diff  and Time_Diff<= 10:
    print("You have been awarded Provincial Scroll")
else:
    print("You have not received an award")
