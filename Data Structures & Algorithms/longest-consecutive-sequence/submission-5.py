class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sum = 0

        for i in range(len(nums)):
            num_sum = 1
            if nums[i] -1 not in num_set:
                r = nums[i]
                while r + 1 in num_set:
                    num_sum+=1
                    r +=1
                max_sum = max(max_sum, num_sum)  

        return max_sum          
               

