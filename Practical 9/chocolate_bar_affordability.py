#This code functions to determine how many chocolate bars the user is able to afford at the supermarket
#use the define function
#calculate the number of chocolate bars affordable by dividing the total money the user has by the price of one chocolate bar
#calculate the change by substracting the money used to buy the number of chocolate bars affordable from the total money
#return the function
def chocolate_bar_affordability(total_money,price):
    number_of_bars = int(total_money / price)
    change = total_money - (number_of_bars * price)
    print(f"The number of bars that can be bought is {number_of_bars}")
    print(f"The change that will be left over is {change} ")
    return (number_of_bars, change)

print(chocolate_bar_affordability(100,8))
    