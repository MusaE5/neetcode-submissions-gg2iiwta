class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best_sum = 0

        for i in range(len(nums)):
            if nums[i] -1 not in num_set:
                length=1
                current_num = nums[i]

                while current_num +1 in num_set:
                    length+=1
                    current_num+=1

                best_sum = max(best_sum, length)

        return best_sum                        



        