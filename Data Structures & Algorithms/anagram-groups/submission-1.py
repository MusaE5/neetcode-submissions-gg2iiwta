class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in hash:
                hash[key] = []

            hash[key].append(strs[i])

        return list(hash.values())        