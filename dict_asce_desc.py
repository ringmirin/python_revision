### write a python program to sort(ascending and descending) a dictionary by value.

my_dict={"a":2,"d":6,"e":3,"f":5}
l=sorted(my_dict.values())
dict1={}
for i in l:
   for k in my_dict.keys():
      if my_dict[k]==i:
         dict1[k]=my_dict[k]        
print(dict1)
l=sorted(my_dict.values(),reverse=True)
dict2={}
for i in l:
   for k in my_dict.keys():
      if my_dict[k]==i:
         dict2[k]=my_dict[k]
print(dict2)


####
my_dict={"a":2,"d":6,"e":3,"f":5}
import operator
dict1=sorted(my_dict.items(), key=operator.itemgetter(1))
print(dict1)
dict2=sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
print(dict2)