#GFG #Problem of the day

#K Sized Subarray Maximum

#Approach used :-  Sliding window with Additional space

#Time Complexity :- O(n)
#Space Complexity :- O(k)

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        q = []  
        result = []  
        for i in range(len(arr)):  
            while q and arr[i] >= arr[q[-1]]:  
                q.pop()  
            q.append(i)  
            # Remove elements out of the current window from the front  
            while q[0] <= i - k:  
                q.pop(0)  
                
            # Now window size is equal to k. Lets add max element.
            if i >= k - 1:  
                result.append(arr[q[0]])  
        return result
