#program to count occurence of each word and find the maximum recurring word.
file = open("hello.txt",'r')
newlst = dict()
for word in file:
    lst = word.strip().split()
    for item in lst:
        newlst[item] = newlst.get(item,0)+1

for key in newlst:
    print(key,newlst[key])
maxWord = max(newlst.values())
print(list(newlst.keys())[list(newlst.values()).index(maxWord)]+":"+str(maxWord))

