def chocolate_bar_affordability(total_money,price):
    number_of_bars = int(total_money / price)
    change = total_money - (number_of_bars * price)
    print(f"The number of bars that can be bought is {number_of_bars}")
    print(f"The change that will be left over is {change} ")
    return (number_of_bars, change)

print(chocolate_bar_affordability(100,8))
    