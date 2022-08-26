s=input("enter: ")
def fun1(s):
   for i in range(len(s)):
      if s[i].isalnum():
         return True
      # break
   return False
print(fun1(s))
def fun2(s):
   for i in range(len(s)):
      if s[i].isalpha():
         return True
      # break
   return False
print(fun2(s))
def fun3(s):
   for i in range(len(s)):
      if s[i].isdigit():
         return True
      # break
   return False
print(fun3(s))
def fun4(s):
   for i in range(len(s)):
      if s[i].isupper():
         return True
      # break
   return False
print(fun4(s))
def fun5(s):
   for i in range(len(s)):
      if s[i].islower():
         return True
   return False
print(fun5(s))


