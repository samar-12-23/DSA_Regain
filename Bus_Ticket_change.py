#GFG #Problem of the day

#Approach used :- Greedy Approach 

#Time complexity:- O(n)
#Space complexity :- O(1))

class Solution:
  def canServe(self,arr):
    count_5=0
    count_10=0
    count_20=0
    for i in range(len(arr)):
      if arr[i]==5:
        count_5+=1
      if arr[i]==10:
        count_10+=1
        if count_5>0:
          count_5-=1
        else:
          return False
      if arr[i]==20:
        count_20+=1
        if count_10>0:
          count_10=-1
          if count_5>0:
            count_5-=1
          else;
          return False
        elif count_5>2:
          count_5-=3
        else:
          return False
    return True


  
