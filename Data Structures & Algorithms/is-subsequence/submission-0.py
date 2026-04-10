class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        i = 0
        
        while i<len(t) and index<len(s):
            if s[index] == t[i]:
                index+=1
            i+=1

        if index == len(s):
            return True
        else:
            return False            




        