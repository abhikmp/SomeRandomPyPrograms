#program to count number of words in a text file
file = open("hello.txt",'r')
newlst = dict()
for word in file:
    lst = word.strip().split()
    for item in lst:
        newlst[item] = newlst.get(item,0)+1

maxWord = max(newlst.values())
print(list(newlst.keys())[list(newlst.values()).index(maxWord)]+":"+str(maxWord))

