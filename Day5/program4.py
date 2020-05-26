# problem on knapsack

def knpsk(wht, List):
    if wht == 0 or len(List) == 0:
        return 0
    if len(List) == 1:
        if List[0][0] > wht:
            return 0 
        return List[0][1]  
    if List[0][0] > wht:
        return knpsk((wht, List[1:]))
    return max(List[0][1] + knpsk(wht - List[0][0], List[1:]), knpsk(wht, List[1:]))
size =  int(input("Number of items you want to enter: "))
List = []
for i in range(size):
    wht = int(input("Enter the wht for item number " + str(i + 1) + ": "))
    value = int(input("Enter the value for item number " + str(i + 1) + ": "))
    List.append((wht,value))
wht = int(input("Enter the value of wht capacity: "))
print("The maximum value for a given pair is: ", knpsk(wht, List))
