bf = open('data.bin', 'wb')
bf.write(b'h\xFFa\xEEc\xDDk\n') # Write binary data in a bytes
bf.close()
open('data.bin', 'rb').read() # Read binary data to a bytes

tf = open('unidata.txt', 'w', encoding='utf-8')
tf.write('h\u00c4ck')
tf.close()

open('unidata.txt', 'r', encoding='utf-8').read()      # Decodes from UTF-8

open('unidata.txt', 'rb').read()                       # Raw encoded text