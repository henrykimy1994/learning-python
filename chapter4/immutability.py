s = 'Code'

# Immutable objects cannot be changed
s[0] = 'z'

# But we can run expressions to make new objects
s = 'z' + s[1:]

L = list(s)

L[0] = 'c'

''.join(L)

B = bytearray(b'app')
B.extend(b'lication')
B.decode()
