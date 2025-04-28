s = 'Code'
s.find('od')
s.replace('od', 'abl')

line = 'aaa,bbb,cccc,dd'
line.split(',')

s.upper()

# content tests
s.isalpha()

line = 'aaa,bbb,cccc,dd\n'
line.rstrip()
line.rstrip().split(',')

tool = 'Python'
major = 3
minor = 3

'Using %s version %s.%s' % (tool, major, minor + 9)
'Using {} version {}.{}'.format(tool, major, minor + 9)
f'Using {tool} version {major}.{minor + 9}'