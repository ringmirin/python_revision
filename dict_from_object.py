###  Write a Python program to remove duplicates from Dictionary
dict1={"red":9,
"pink":6,
"white":2,
"black":6}

temp=[]
dic={}
for key, value in dict1.items():
   if value not in temp:
      temp.append(value)
      dic[key]=value
print(dic)

