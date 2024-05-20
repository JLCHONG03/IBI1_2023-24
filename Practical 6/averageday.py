#import necessary libraries
#store the data in dictionary
#create an "other" variable and count the hour spent on it 
#add the "other" variable into the dictionary
#plot a pie chart for the data in the dictionary
import matplotlib.pyplot as plt 

Activity ={
    'Sleeping': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1
}

Total_hours_in_a_day = 24
Time_spent = sum(Activity.values())
Others = Total_hours_in_a_day - Time_spent
Activity['Others'] = Others

plt.figure() 
plt.pie(Activity.values(), labels=Activity.keys(), startangle = 90)
plt.title("Average day of a univeristy student")
plt.show()
plt.clf()
#print the number of hours spent on a specific activity 
Interested_activity = 'Classes'
print(f"Number of hours spent on {Interested_activity}: {Activity.get(Interested_activity, 0)}")


