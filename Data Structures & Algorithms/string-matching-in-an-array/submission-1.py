class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    result.add(words[i])
                elif words[j] in words[i]:
                    result.add(words[j])  
        return list(result)            

                   




        