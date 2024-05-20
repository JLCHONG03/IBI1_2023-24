a = 40
b = 36
c = 30
d = a-b #let d as the time improvement after the first training
e = b-c #let e as the time improvement after the second training
print(d)
print(e)
if d < e: #Compare the time improvement between the two training
    print("e is greater")
    print("second training has a better improvement") 
else:
    print("d is greater")
    print("first training has better improvement")

X = a < b 
Y = b < c
W = not (X and Y) #The opposite result of the 'AND' truth table 
print(X,Y,W)      # AND Truth Table
                  # A    B     A and B
                  # True True  True 
                  # True False False
                  # False True False
                  # False False False

