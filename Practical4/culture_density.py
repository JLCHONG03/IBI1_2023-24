ccd = 5 #let the initial cell culture density as 5%
d = 1 #let the first day as 1
print("Day ", str(d), " = ", str(ccd))
while ccd<=90: #the cell culture density cannot exceed 90%
    ccd = 2*ccd #the cell culture density doubles per day
    d = d + 1
    print("Day ", str(d), " = ", str(ccd))
    if ccd>90: #stop when the cell culture density exceeds 90%
        break
print("On Day 6 the cell culture density is higher than 90%")