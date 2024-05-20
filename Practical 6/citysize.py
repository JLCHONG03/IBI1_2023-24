#import the necessary libraries
#store the data
import matplotlib.pyplot as plt 

uk_cities = [0.56, 0.62, 0.04, 9.7]
uk_names = ["Edinburgh", "Glasglow", "Stirling", "London"]
china_cities = [0.58, 8.4, 29.9, 22.2]
china_names = ["Haining", "Hangzhou", "Shanghai", "Beijing"]

#sort the population sizes using the sorted function
#print the sorted values
sort_uk_cities = sorted(uk_cities)
sort_china_cities = sorted(china_cities)
print("Sorted values for the populations of cities in the UK:", sort_uk_cities)
print("Sorted values for the populations of cities in China:", sort_china_cities)

#plot the a bar chart for the data 
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)#use the subplot function to plot two bar chart in one figure
plt.bar(uk_names, uk_cities)
plt.title("Population of UK cities in 2024")
plt.xlabel("Cities in UK")
plt.ylabel("Population (in million)")

plt.subplot(2,1,2)
plt.bar(china_names, china_cities)
plt.title("Population of China cities in 2024")
plt.xlabel("Cities in china")
plt.ylabel("Population (in million)")
plt.tight_layout()#adjust the spacing between two bar plots
plt.show()
plt.clf()

