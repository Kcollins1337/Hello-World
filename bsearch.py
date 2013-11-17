def bsearch(List, searchFor):
   for i in List:
       if i == searchFor:
           return i
   

list = [n for n in range(100)]
value = 8
print bsearch(list, value)
