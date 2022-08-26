#### Write a Python program to combine two dictionary adding values for common keys.

# while loop
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
n=list(d1)
m=list(d2)
d3={}
i=0
while i<len(n):
   if n[i] in m[i]:
      d3[n[i]]=d1[n[i]]+d2[m[i]]
   else:
      d3[n[i]]=n[i]=d1[n[i]]
      d3[m[i]]=m[i]=d2[m[i]]
   i+=1
print(d3)











