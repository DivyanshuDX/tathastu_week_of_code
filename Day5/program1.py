#to replace every element with the greatest element on the right side

def replace(List):
    for i in range(size-1):
        List[i] = max(List[i+1:])
    return List
size = int(input("Enter the size of the list: "))
List = []
for i in range(size):
    List.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("The list after replacing every element with the greatest no is: ", replace(List))
