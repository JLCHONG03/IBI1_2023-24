# What does this piece of code do?
# Answer:Sum of 100 random numbers between 1 and 10

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0#let the progress start from 0
total_random_number=0#let the total random number start from 0
while progress<100:#while the progress
	progress+=1#the progress increased by 1 per loop
	n = randint(1,10)#a random number is chose from 1 to 10
	total_random_number = total_random_number+n#the randomly rolled number n is added to the total random number

print(total_random_number)
