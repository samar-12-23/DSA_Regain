#GFG #Problem of the day

#Approach used :- sliding window with usage of map (Optimised solution)
# Time complexity -> O(N)
# Space complexity -> O(K)

class Solution:
    def countAtMostK(self, arr, k):
        if k == 0:
            return 0

        freq = {}
        left = 0
        distinct = 0
        count = 0

        for right in range(len(arr)):
          
            if arr[right] not in freq or freq[arr[right]] == 0:
                distinct += 1
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1

          
            count += (right - left + 1)

        return count
