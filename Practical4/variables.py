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

X = True
Y = True
W = X != Y 
# W Truth Table
# X    Y     W
# True True  False 
# True False True
# False True True
# False False False

print('W: ', W)
