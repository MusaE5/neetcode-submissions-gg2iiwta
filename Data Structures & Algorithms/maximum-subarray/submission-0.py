class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSub = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum<0:
                currentSum = 0
            currentSum +=n
            maxSub = max(maxSub, currentSum)   

        return maxSub     

            





        