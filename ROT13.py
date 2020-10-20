
import string
def ROT13(s):
    l3 = []
    l1 = list(string.ascii_lowercase[:13]+string.ascii_uppercase[:13])
    l2 = list(string.ascii_lowercase[13:]+string.ascii_uppercase[13:])
    for chars in s:
        if chars in l1:
            l3.append(l2[l1.index(chars)])
        elif chars in l2:
            l3.append(l1[l2.index(chars)])
        else:
            l3.append(chars)
    return("".join(l3))


############## Main program ##################
s = input("Enter string to be encrypted or decrypted")
print(ROT13(s))

