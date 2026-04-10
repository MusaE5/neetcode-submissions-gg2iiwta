class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
    
        for n in range(len(strs)):
            signature = "".join(sorted(strs[n]))  
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(strs[n])     
    
        return list(groups.values())              