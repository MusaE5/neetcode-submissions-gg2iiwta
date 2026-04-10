class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majority = n//3
        hash_map = {}
        result = []

        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1

        for num, freq in hash_map.items():
            if freq > majority:
                result.append(num)

        return result        


        