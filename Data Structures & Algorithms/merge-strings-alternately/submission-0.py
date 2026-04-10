class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length = min(len(word1), len(word2))

        l = 0
        word = []

        while l< length:
            word.append(word1[l])
            word.append(word2[l])
            l+=1

        if len(word1) < len(word2):
            word.append(word2[l:])  
        else:
            word.append(word1[l:])  

        word = ''.join(word)

        return word





        