filename = './templates/positive-words.txt'

a = open(filename, 'r').read()
b = a.split('\n')
print(len(b))
