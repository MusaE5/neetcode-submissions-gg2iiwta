class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = {}
        for c in s1:
            if c not in freq1:
                freq1[c] = 1
            else:
                freq1[c] += 1

        window_size = len(s1)
        freq2 = {}      
    
        if len(s1) == 1:
            return s1[0] in s2

        for i in range(len(s1)):
            if s2[i] not in freq2:
                freq2[s2[i]] = 0
            freq2[s2[i]] +=1
  

        l, r = 0, len(s1) -1

        while r<len(s2)-1:
            if freq2 == freq1:
                return True 
            elif r<len(s2) -1:
                freq2[s2[l]] -=1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                r+=1
                l+=1
                if s2[r] not in freq2:
                    freq2[s2[r]] = 0
                freq2[s2[r]] +=1

        return freq1 == freq2                         









        
               




         





            





        