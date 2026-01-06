#GFG #Problem_of_the_day

# First Approach( T(n) -> O(n) )   -- Sliding window with K 
class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n=len(arr)
        maxi_xor=0
        
        for i in range(n-k+1):
            curr_xor=0
            for j in range(i,i+k):
                curr_xor^=arr[j]
                
            maxi_xor=max(maxi_xor,curr_xor)
            
        return maxi_xor


# Second Approach ( T(n) -> O(n) )  --Prefix sum

class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n = len(arr)
        prefix = [0] * (n + 1)

        # Build prefix XOR
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        max_xor = 0

        # XOR of subarray [i, i+k-1] = prefix[i+k] ^ prefix[i]
        for i in range(n - k + 1):
            curr_xor = prefix[i + k] ^ prefix[i]
            max_xor = max(max_xor, curr_xor)

        return max_xor
        
        
        


        
        
        

