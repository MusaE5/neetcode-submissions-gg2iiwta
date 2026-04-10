class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        index_map = {}
        old_strs = strs[:]
        sorted_anagrams = []

        for i in range(len(strs)):
            strs[i] = ''.join(sorted(strs[i]))

        for j in range(len(strs)):
            if strs[j] not in index_map:
                index_map[strs[j]] = []     
            index_map[strs[j]].append(j)

        for indices in index_map.values():
            group = []
            for i in indices:
                group.append(old_strs[i])
            sorted_anagrams.append(group)

        return sorted_anagrams         











        