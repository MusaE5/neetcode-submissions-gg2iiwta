class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        index = {}
        result = []

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in index:
                index[key] = [i]
            else:
                index[key].append(i)

        for value in index.values():
            sub_arr = []
            for i in range(len(value)):
                sub_arr.append(strs[value[i]])
            result.append(sub_arr)

        return result        










        
         
          










        