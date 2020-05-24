# to find the permutation of the given list
  
def permutation(List, String = ""):
    Set = set(List)
# set() --> A Set is an unordered collection  
#            data type that is iterable, mutable,  
#            and has no duplicate elements. 
    stringList = []
    if len(Set) == 1:
        String += "".join(List)
# "".join() --> It joins two adjacent elements in 
#               iterable with any symbol defined in  
#               "" ( double quotes ) and returns a  
#               single string

        return list([String])
    for i in Set:
        List1 = list(List)
        S = String + i
        List1.remove(i)
        stringList.extend(permutation(List1, S))
    return stringList

string = input("Enter a string: ")
List = permutation(list(string))
print("All the permutation of the string is: " + ", ".join(List))
