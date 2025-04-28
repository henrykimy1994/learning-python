D = dict(a=1, b=2, c=3)

list(D.keys())
list(D.values())
list(D.items())

for key in D.keys():               
    print(key, '=>', D[key])

for (key, value) in D.items():
    print(key, '=>', value)