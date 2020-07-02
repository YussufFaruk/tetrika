with open('names.txt','r') as f:
    names = f.read()

nameslist = names.split(',')

for i in range(len(nameslist)):
    nameslist[i] = nameslist[i].strip('"')

nameslist.sort()

s1 = 0

for i in range(len(nameslist)):
    s = 0
    for k in range(len(nameslist[i])):
        s += ord(nameslist[i][k]) - 64
    s1 += s*(i+1)

print(s1)
