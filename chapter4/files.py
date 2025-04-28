f = open('data.txt', 'w') #in text-output mode

f.write('Hello\n')

f.write('world!\n') 

f.close()

f = open('data.txt')

text = f.read()

text

text.split()

for line in open('data.txt'):       # Display lines in a file
    print(line.rstrip())            # Single spaced (sans \n)