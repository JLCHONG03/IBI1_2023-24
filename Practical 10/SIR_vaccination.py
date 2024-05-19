#define a new "vaccine" variable
#set the initial vaccination number as 10%
#create an array for this variable too
#change the probability of infection because the vaccination rate has to be counted
#plot the infected number of the current vaccination rate

import numpy as np
import matplotlib.pyplot as plt

Infected = 1
Population = 10000
Recovered = 0
Susceptible = Population - Infected
Vaccination_rate = 0.2
Vaccinated = Population * Vaccination_rate
beta = 0.3
gamma = 0.05
        
S = [Susceptible]
I = [Infected]
R = [Recovered]
V = [Vaccinated]
    
for time in range(1,1000):
    probability_of_infection = beta * (I[-1] + V[-1])/ Population
    probability_of_recovery = gamma
            
    new_infected = np.random.choice([0,1],S[-1],[1-probability_of_infection,probability_of_infection])
    new_recovery = np.random.choice([0,1],I[-1],[1-probability_of_recovery,probability_of_recovery])
            
    S.append(S[-1] - np.sum(new_infected))
    I.append(I[-1] + np.sum(new_infected) - np.sum(new_recovery))
    R.append(R[-1] + np.sum(new_recovery))
    V.append(V[-1])
        
plt.figure()    
plt.plot(I, label="20%")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR")
plt.legend()
plt.show()
plt.clf