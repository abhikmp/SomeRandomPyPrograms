import csv
def addtocsv(lst):
    with open('filename.csv', 'w') as csvfile:     #enter a file name here
        writer = csv.writer(csvfile)
        for item in lst:
            writer.writerow(item)
    csvfile.close()


to_csv = []
lst = ""
columns = input("Enter the column-names")
print(columns)
while(1):
    lst = input()
    if lst!="":
        to_csv.append(lst.rstrip().split())
    else:
        break

addtocsv(to_csv)
print(to_csv)