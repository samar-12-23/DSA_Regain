#GFG #Random Problem Solving 

#Approach Used :- Two Pointers

#Time Complexity -> O(n)
#Space complexity -> O(1)

class Solution:
    def reverseArray(self, arr):
        # code here
        start=0
        end=len(arr)-1
        while start<end:
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
        return arr

#Example  arr=[1,2,3,4,5]
#Solution arr= [5,4,3,2,1]
        
        
        
