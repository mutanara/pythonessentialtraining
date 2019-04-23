 #first_way (where you just tell the sequence where to stop)

y = range (5)
for x in y:
    print("x is {}".format(x))

#second_way ( where you tell a sequence where to start and stop)

y = range (6, 10)
for x in y:
    print("x is {}".format(x))

#third_way (where you tell a sequence where to start, stop and the interval between variables)

y = range (11, 20, 3)
for x in y:
    print("x is {}".format(x))

#in all the three ways above, the range sequence never considers the closing number.