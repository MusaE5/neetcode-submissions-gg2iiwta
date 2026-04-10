class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = set()
        max_length = 1
        l = 0
        if s:
            dupes.add(s[0])
        else:
            return 0

        for r in range(1, len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l +=1
            dupes.add(s[r])

            max_length = max(max_length, len(dupes)) 

        return max_length    




        