### When provided with a letter, return its position in the alphabet.
 
def position(alphabet):
   alph="abcdefghijklmnopqrstuvwxyz"
   i=1
   while i<len(alph):
      if alphabet in alph[i]:
         res=i+1
      i+=1
   return res
print(position("e"))
