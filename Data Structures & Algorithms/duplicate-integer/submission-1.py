class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for i in range(len(nums)):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                return True
        return False

        