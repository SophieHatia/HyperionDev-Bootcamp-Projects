CyclingTime= input("Time taken to complete cycling section= ")
RunningTime = input("Time taken to complete running section= ")
SwimmingTime = input("Time taken to complete swimming section= ")

TotalTime = float(CyclingTime)+float(RunningTime)+float(SwimmingTime)
print(TotalTime)

TimeDiff = TotalTime - 100

if TimeDiff <= 0:
    print("You have been awarded Provincial Colours ")
elif 1<= TimeDiff and TimeDiff <= 5:
    print("You have been awarded Provincial Half Colours")
elif 6<= TimeDiff  and TimeDiff<= 10:
    print("You have been awarded Provincial Scroll")
else:
    print("You have not received an award")
