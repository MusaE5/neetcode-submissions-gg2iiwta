class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = len(nums) // 3
        freq = {}
        elements = []

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1

        for key, value in freq.items():
            if value > target:
                elements.append(key)

        return elements             







        