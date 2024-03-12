#defining variables setting out the number of rows 
#defining last  row as double the median number of rows
row_median = 5
first_row = 1
last_row = (2*row_median)

#iterating over the full pattern from the first row to the last
for row_number in range(first_row,last_row):

#creating an if statement so that if the row number the code is on is smaller or the same as the median row
#the number of stars printed is the same as the row number -> the number of stars increases
#then if the fow number is larger the number of stars decreases
    if row_number <= row_median:
        stars = row_number
        print(stars * "*", end= " ")
    else:
        stars = last_row - row_number
        print(stars * "*", end=" ")
    
    print()

