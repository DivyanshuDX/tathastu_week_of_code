#to find the no. of occurence in a tuple

size = int(input("Enter the size of tuple: "))
print("Enter the elements in tuple one by one")
ar = []
for i in range(size):
    ar.append(input())
ar = tuple(ar)
element = input("Enter the element whose occurrences you want to know: ")
print("Tuple contains the element", element , " = " , ar.count(element), "times")
