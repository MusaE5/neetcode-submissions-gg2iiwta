class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hash = {}
        groups = []
        for i in range (len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in hash:
                hash[key] = []

            hash[key].append(strs[i])

        return list(hash.values())    



