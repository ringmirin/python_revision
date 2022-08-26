# Write a program to determine if the two given numbers are coprime. A pair of numbers are coprime if their greatest shared 
# factor is 1.

# The inputs will always be two positive integers between 2 and 99.

def co_prime(n,m):
   hcf=1
   for i in range(1,n+1):
      if n%i==0 and m%i==0:
         hcf=i
   return hcf==1
a=int(input("enter the no.:"))
b=int(input("enter the no.:"))
if co_prime(a,b):
   print(True)
else:
   print(False)
print(co_prime(a,b))


