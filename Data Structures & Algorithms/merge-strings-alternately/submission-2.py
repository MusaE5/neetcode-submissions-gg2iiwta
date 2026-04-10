class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            word.append(word1[i])
            word.append(word2[i])

        if len(word1) < len(word2):
            word.append(word2[len(word1):len(word2)])
        elif len(word1) > len(word2):
            word.append(word1[len(word2):len(word1)])

        word = ''.join(word)

        return word    
                