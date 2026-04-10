class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = {}

        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates[nums[i]] = []
            duplicates[nums[i]].append(i)

        for key, value in duplicates.items():
            if len(value) >=2:
                l = 0
                r = len(value)-1
                for j in range(1, len(value)):
                    if value[j] - value[j-1] <=k:
                        return True
                          

        return False                
        






        