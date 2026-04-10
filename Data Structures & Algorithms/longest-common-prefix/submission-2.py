class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        for i in range(len(strs[0])):
            c = strs[0][i]

            for s in range(len(strs)):
                if i >= len(strs[s]) or strs[s][i] != c:
                    return prefix
            prefix += c
        return prefix             
