#import the necessary libraries
#input the initial number for the variable
#create array for the variables
#use the for range loop to loop 1000 time points
#find the probability of infection and recovery(learn from youtube video)
#random choose the new infected and new recovery in the population using the previous number of susceptible and infected and the probability above
#append the new infected and new recovery number into the array
#plot the S, I, and R variable

import numpy as np
import matplotlib.pyplot as plt

Infected = 1
Population = 10000
Recovered = 0
Susceptible = Population - Infected
beta = 0.3
gamma = 0.05
        
S = [Susceptible]
I = [Infected]
R = [Recovered]
    
for time in range(1,1000):
    probability_of_infection = beta * I[-1] / Population
    probability_of_recovery = gamma
            
    new_infected = np.random.choice([0,1],S[-1],[1-probability_of_infection,probability_of_infection])
    new_recovery = np.random.choice([0,1],I[-1],[1-probability_of_recovery,probability_of_recovery])
            
    S.append(S[-1] - np.sum(new_infected))
    I.append(I[-1] + np.sum(new_infected) - np.sum(new_recovery))
    R.append(R[-1] + np.sum(new_recovery))
        
plt.figure(figsize=(10,6))    
plt.plot(S, label="Susceptible")
plt.plot(I, label="Infected")
plt.plot(R, label="Recovery")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR")
plt.legend()
plt.show()
plt.clf


        
        
            
        


