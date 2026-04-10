class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = set()
        max_length = 1
        length = 1

        l, r = 0,1
        if s:
            dupes.add(s[l])
        else:
            return 0    

        while r<len(s):
            while s[r] in dupes:
                dupes.remove(s[l])
                l+=1
            dupes.add(s[r]) 
            r+=1
            max_length = max(max_length, len(dupes))   

        return max_length        












                

        



        