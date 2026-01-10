#GFG #Problem of the day

# Approach used :- Sliding with window & hashmap(dict)

#Time complexity:- O(n)
#Space complexity :- O(1)

#Using In-built library (collections(defaultdict))
class Solution:
    def countSubstr(self, s, k):
        from collections import defaultdict
        
        def at_most_k(s, k):
            count = 0
            left = 0
            freq = defaultdict(int)
            
            for right in range(len(s)):
                freq[s[right]] += 1
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                count += right - left + 1
            return count
        
        return at_most_k(s, k) - at_most_k(s, k - 1)


#Without using in-built library
class Solution:
    def countSubstr (self, s, k):
        return self.atMostK(s , k) - self.atMostK(s , k-1)
    def atMostK(self , s , k):
        if k == 0:
            return 0
            
        d = {}
        length = len(s)
        i = 0
        j = 0
        ans = 0
        
        while j < length:
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            
            while i < j and len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
            
            ans += j-i+1
            
            j += 1
        
        return ans
        


