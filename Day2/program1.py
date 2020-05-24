n = int(input("Enter a number: "))
N = str(n)
L = len(N)
# Program to check if a number is prime or not

# prime numbers are greater than 1
if n > 1:
   # check for factors
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(n,"is not a prime number")

# now it will check the number is odd or even

if (n//2) == 0:
    print(n,"is even")
else:
    print(n,"is odd")

# now it will check for palandrome

temp = n
rev = 0
while(n>0):
    dig = n%10
    rev = rev*10 + dig
    n = n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

#now it will check an Armstrong number

num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
