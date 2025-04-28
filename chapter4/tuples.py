T = (1, 2, 3, 4) 
T + (5, 6)
T[0], T[1:]

T.index(4)

T.count(4)

T[0] = 2  #TypeError: 'tuple' object does not support item assignment

T = (2,) + T[1:]

T = 'hack', 3.0, [11, 22, 33]

T.append(4) #AttributeError: 'tuple' object has no attribute 'append'
