# Create a function with two arguments that will return an array of the first (n) multiples of (x).

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

def count(x,n):
   list=[]
   i=1
   while i<=n:
      m=i*x
      list.append(m)
      i+=1
   return list
print(count(2,8))