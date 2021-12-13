N = int(input())
listi =[]
i=0
for _ in range(N):
    commands = input().split()
    listi.append(commands)
outputlist = []
for l in listi:
    if l[0]=="insert":
        outputlist.insert(int(l[1]), int(l[2]))
    elif l[0]=="print":
        print(outputlist)
    elif l[0]=="remove":
        outputlist.remove(int(l[1]))
    elif l[0]=="append":
        outputlist.append(int(l[1]))
    elif l[0]=="sort":
        outputlist.sort()
    elif l[0]=="pop":
        outputlist.pop()
    elif l[0]=="reverse":
        outputlist.reverse()