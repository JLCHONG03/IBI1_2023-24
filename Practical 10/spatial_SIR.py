#import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # Set the chosen point to infected (1)

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.show()
plt.clf()

#input the initial value for beta and gamma
beta = 1/8
gamma = 0.1
#use define function to infect neighbors
def infect_neighbors(i, j):
    #infect each neighbour with probability beta
    #infect all 8 neighbours
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            #don't infect yourself!
            if (x,y) != (i,j):
                if 0 <= x < 100 and 0 <= y < 100:  #make sure I don't fall off an edge
                    if population[x, y] == 0:  #only infect neighbours that are not already infected!
                        if np.random.rand() < beta:  # Probability of infection
                            population[x, y] = 1  # Infect the neighbor

#loop 100 time points
for t in range(1,100):
    infected_points = np.where(population == 1)  #find infected points
    for i, j in zip(infected_points[0], infected_points[1]):
        infect_neighbors(i, j)  #infect the neighbors
        if np.random.rand() < gamma:  # Probability of recovery
            population[i, j] = 2  # Recover the infected individual

# Plot the outcome
plt.figure(figsize=(8, 6))
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.colorbar(label='State (0:Susceptible, 1:Infected, 2:Recovered)')
plt.title('Spatial SIR Model')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()