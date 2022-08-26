def Binary(n):
   s = bin(n)[2:]

   # removing "0b" prefix
   # s1 = s[2:]
   s=s.split("1")
   turns=len(s)+len(s[-1])-2
 
# print("The binary representation of 100 (using bin()) is : ", end="")/
print(Binary(128))