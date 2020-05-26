#the max value a thief can steal from any house

def home(List):
    if len(List) == 1:
        return List[0]
    if len(List) == 2:
        return max(List)
    if len(List) == 3:
        return max(List[1], List[0] + home(List[2:]))
    return max(List[1] + home(List[3:]), List[0] + home(List[2:]))
size = int(input("Enter the number of homes in a line: "))
List = []
for i in range(size):
    List.append(int(input("Enter the value in the home number " + str(i + 1) + ": ")))
print("The maximum stolen value from homes is", home(List))
