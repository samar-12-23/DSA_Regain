#GFG #Problem of the day
#Count distinct elements in every window

#Brute Force Approach :- Nested loop with sliding window --> T(n) - > O(n*k) , Space Complexity -> O(k)
#Optimised Approach :- Sliding window + Hashmap(set)  --> T(n) -> O(n) , Space Complexity -> O(k)

class Solution:
    def countDistinct(self,arr, k):
        n = len(arr)
        freq = {}
        result = []
    
        # Step 1: First window
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
    
        result.append(len(freq))
    
        # Step 2: Slide the window
        for i in range(k, n):
            # Remove outgoing element
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
    
            # Add incoming element
            incoming = arr[i]
            freq[incoming] = freq.get(incoming, 0) + 1
    
            result.append(len(freq))
    
        return result
            
            
