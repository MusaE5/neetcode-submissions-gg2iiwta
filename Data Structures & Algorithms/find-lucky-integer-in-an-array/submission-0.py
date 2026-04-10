class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq = {}
        max_num = float('-inf')

        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] +=1


        for key, value in freq.items():
            if key == value:
                max_num = max(max_num, key)
                
        if max_num == float("-inf"):
            return -1       

        return max_num        

        