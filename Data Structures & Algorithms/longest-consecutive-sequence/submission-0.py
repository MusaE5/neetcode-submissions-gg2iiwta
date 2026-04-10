class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for i in range (len(nums)):
            if nums[i] -1 not in num_set:
                current_num = nums[i]
                length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1

                max_length = max(length, max_length)    

        return max_length                
