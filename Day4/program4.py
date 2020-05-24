#remove duplicate values accross bary values

a = int(input("Enter the no of items you want to add in Dictonary: "))
b = dict()
for i in range(a):
    key = input("Enter the key for item " + str(i + 1) + " in dictonary: ")
    value = int(input("Enter the value for item " + str(i + 1) + " in dictonary: "))
    b[key] = value
result = dict()
for key,value in b.items():
    if value not in result.values():
        result[key] = value
print("Dictonary after removing duplicate values: ", result)
