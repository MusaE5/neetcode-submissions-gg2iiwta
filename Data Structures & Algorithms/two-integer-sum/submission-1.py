class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for n in range(len(nums)):
            complement = target - nums[n]
            if complement not in hash:
                hash[nums[n]] = n
            else:
                return [hash[complement], n]    




