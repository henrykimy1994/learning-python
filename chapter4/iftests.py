D = {'a': 1, 'b': 2, 'c': 3}

# Referencing a nonexistent key is an error
D['e']   

'e' in D 

D.get('a', 'missing')

D['e'] if 'e' in D else 0