D = {'name': 'Pat', 'job': 'dev', 'age': 40}

D['name'] 
D['job'] = 'mgr'

D = {}
D['name'] = 'Pat'

pat1 = dict(name='Pat', job='dev', age=40) 
pat2 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))