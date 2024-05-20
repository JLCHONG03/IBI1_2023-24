#import the necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:\\Users\\JL CHONG\\Desktop\\IBI1\\IBI1_2023-24\\Practical 7")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#print(dalys_data.head(6)) #access the first 6 data
#print(dalys_data.info()) #check the details of the data (the number of rows and columns of the data )
#print(dalys_data.describe()) #check the statistics of the data(mean, range, standard deviation)
#iloc can help us to access the data by the number of row and column eg.[row number, column number]
#print(dalys_data.iloc[0,3]) #first row and second column
#print(dalys_data.iloc[2,0:5]) #third row and the first to fourth column
#print(dalys_data.iloc[0:2,:]) #first two row and all columns
#print(dalys_data.iloc[0:10:2,0:5]) #first tenth row with a step of 2, eg the 0, 2nd, 4th, 6th and etc. First to fourth column
#print(dalys_data.iloc[0:10:2,0:4]) #first tenth row with a step of 2, eg the 0, 2nd, 4th, 6th and etc. First to third column

#first 100 rows with a step of 10, fourth column
print(dalys_data.iloc[0:101:10,3])

#use Boolean to access the entries
#print(dalys_data.iloc[0:3,[0,1,3]])#first three row, first four column but excluding the second
#my_columns = [True, True, False, True]
#print(dalys_data.iloc[0:3,my_columns])#read the columns with Boolean = True
#loc can help to access data by the headings of the data
#print(dalys_data.loc[2:4,"Year"])#second to fourth row, data in the "Year" heading column
#print(dalys_data.loc[0:29,"DALYs"])#first to 29th row, data in the "DALYs" heading column

#rows where the heading 'Entity; is 'Afghanistan' and the "DALYs" column
print(dalys_data.loc[dalys_data['Entity'] == 'Afghanistan', 'DALYs'])

china_columns = [True, False, True, True]
China = dalys_data.loc[dalys_data['Entity'] == 'China', china_columns]
print(China)
China_DALYs = China.loc[0:, 'DALYs']
China_mean = np.mean(China_DALYs)#compute the mean DALYs in China
print('The mean DALYs in China:', China_mean)
if China_mean > dalys_data.iloc[1169, 3]:
    print("The mean DALYS in China over time is greater than the DALYs measured in 2019")

china_year = China.loc[0:, 'Year']
plt.figure(figsize=(10, 6))
plt.plot(china_year, China_DALYs, 'bo', linestyle='-')#a circle plot in blue was used
plt.title('DALYs over time in China')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.grid(True)#show the grid to have a clearer vision on the graph
plt.xticks(china_year,rotation=-90)#plot all the years in the x-axis and rotate it by 90 degree
plt.show()
plt.clf()


#filter data for the United Kingdom
uk_data = dalys_data[dalys_data['Entity'] == "United Kingdom"]

#plot DALYs over time for the UK
plt.figure(figsize=(10, 6))
plt.plot(uk_data['Year'], uk_data['DALYs'], marker='o', linestyle='-')
plt.title('DALYs Over Time in the United Kingdom')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.grid(True)
plt.show()
plt.clf()
