#to remove the duplicates in a string

def duplicate(string):
    duplicateString = ""
    for i in string:
        if i not in duplicateString:
            duplicateString += i
    return duplicateString

string = input("Enter the string: ")
print("String after removing the duplicates is:", duplicate(string))
