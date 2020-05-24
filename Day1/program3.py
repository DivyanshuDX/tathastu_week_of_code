#to swap between two no. without using third variable

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
a = a + b
b = a - b
a = a - b
print("After swapping")
print("value of a : ", a )
print("value of b : ", b )
