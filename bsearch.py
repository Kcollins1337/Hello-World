# Kalen Collins





def bsearch(List, searchFor):

      high = len(List)-1 # Sets the end of the list
      low = 0 # Sets the start of the list
          
      while low <= high:
         
         if len(List) == 0: # Used to make sure the list is not empty
            return "Empty List"
         
         mid = (high + low)//2 # Sets mid as the halfway point in the list
         
         if List[mid] < searchFor: # If mid is less than searchFor it adds +1 to low
            low = mid + 1
            
         elif List[mid] > searchFor: # If mid is greater than searchFor it subtracts -1 from low
            high = mid - 1
            
         else:
            return mid # Returns mid if mid is neither greater than or less than but equal to searchFor
         
