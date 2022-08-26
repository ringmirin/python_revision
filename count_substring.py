def count_substring(string,sub_string):
   string_length=len(string)
   sub_string_length=len(sub_string)
   times=string_length-sub_string_length
   i=0
   count=0
   while i<=times:
      if string[i:sub_string_length]==sub_string:
         count+=1
      sub_string_length+=1
      i+=1
   return count
print(count_substring("abcdcdccdc","cdc"))







