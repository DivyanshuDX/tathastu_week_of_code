#to print the SQUARE pattern

n = int(input("Enter the Value of N: "))
if n <= 1:
   print("Please enter the no. greater than 1")
else:   
   for i in range(n):
       print("* " * (n - i) + "    " * i + " *" * (n - i))
   for i in range(2,n + 1):
       print("* " * i + "    " * (n - i) + " *" * i)
