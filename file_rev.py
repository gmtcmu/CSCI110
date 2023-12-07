

f = open("States.txt", "rb")
s = f.readlines()
f.close()
f = open("newstates2.txt", "wb")
x = s.reverse()
f.write(x)