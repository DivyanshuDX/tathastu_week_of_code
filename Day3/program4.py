#to enter the no. in the list and remove there duplicates

def duplicate(List):
    duplicateList = []
    for i in List:
        if i not in duplicateList:
            duplicateList.append(i)
    return duplicateList

size = int(input("Enter the no of elements you want to add in List: "))
print("Enter the element in List one by one")
List = []
for i in range(size):
    List.append(input())
print("List after removing the duplicates is:", duplicate(List))
