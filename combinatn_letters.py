### Write a Python program to create and display all combinations of letters, selecting 
### each letter from a different key in a dictionary.

sample_data={'1':['a','b'], '2':['c','d']}
for x in sample_data['1']:
   for y in sample_data['2']:
      print(x+y)