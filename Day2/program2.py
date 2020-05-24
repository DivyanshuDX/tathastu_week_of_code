# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms u want to display fibbonacci series? "))

# first two terms
n1, n2 = 0, 1
num = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while num < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       num += 1
