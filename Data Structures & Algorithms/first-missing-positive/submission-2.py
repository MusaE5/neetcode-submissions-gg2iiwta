class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if 1 not in nums:
            return 1

        maxNum = float('-inf')
        for i in nums:
            maxNum = max(maxNum, i)     

        for i in range(2, maxNum):
            if i not in nums:
                return i
        return maxNum+1        



       



        