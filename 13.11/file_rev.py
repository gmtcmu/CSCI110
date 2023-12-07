

f = open('input.txt', 'r')
copy = open('output.txt', 'w')
for line in f:
    copy.write(line[::-1])


