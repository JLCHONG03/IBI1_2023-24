#use the define function
#store the actors and their corresponding year of acting into a dictionary
#compare the year where an individual turned 18 to the year in the dictionary
#return the function
def favourite_bond_actor(year_borned):
    bond_actors = {(1973,1986): "Roger Moore",
          (1987,1994): "Timothy Dalton",
          (1995,2005): "Pierce Brosnan",
          (2006,2021): "Daniel Craig"}

    year_18 = year_borned + 18
    for (year_start, year_end), actor in bond_actors.items():
            if year_start <= year_18 <= year_end:
                
                return f"An individual's favorite Bond is {actor}."

print(favourite_bond_actor(year_borned=1965))