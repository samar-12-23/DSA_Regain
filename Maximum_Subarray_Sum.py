#Problem of the day #GFG 

#Maximun Subarray Sum Problem using Sliding window Approach

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        maxi=-1
        Sum=sum(arr[0:k-1])
        for i in range(k-1,len(arr)):
            Sum+=arr[i]
            maxi=max(maxi,Sum)
            Sum -= arr[i-k+1]
            
        return maxi

  s=Solution()
