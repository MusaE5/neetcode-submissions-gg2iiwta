class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best_length = 0

        for i in range(len(nums)):
            if nums[i] -1 not in num_set:
                current_num = nums[i]
                length = 1

                while current_num +1 in num_set:
                    current_num += 1
                    length+=1

                best_length = max(best_length, length)

        return best_length         




        