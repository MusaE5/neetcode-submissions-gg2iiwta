class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            word+= word1[i]
            word+= word2[i]

        if len(word1) < len(word2):
            for i in range(len(word1), len(word2), 1):
                word+= word2[i]
        elif len(word1) > len(word2):
            for i in range(len(word2), len(word1), 1):
                word+= word1[i]       

        return word            
        