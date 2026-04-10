class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashMap = {}

        for c in ransomNote:
            if c not in hashMap:
                hashMap[c] = 0
            hashMap[c] +=1

        for c in magazine:
            if c in hashMap:
                hashMap[c] -=1


        for num in hashMap.values():
            if num>0:
                return False
        return True                        


        