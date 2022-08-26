###Write a Python script to check whether a given key already exists in a dictionary

dict1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key=int(input("enter the key: "))
if key in dict1.keys():
   print("exist")
else:
   print("not exist")
   
