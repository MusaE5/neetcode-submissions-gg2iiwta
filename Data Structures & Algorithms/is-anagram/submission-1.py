class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = {}
        freq_2 = {}

        for c in s:
            if c not in freq_1:
                freq_1[c] = 1
            else:
                freq_1[c] +=1

        for c in t:
            if c not in freq_2:
                freq_2[c] = 1
            else:
                freq_2[c] +=1    

        if freq_1 == freq_2:
            return True
        else:
            return False    




        
        