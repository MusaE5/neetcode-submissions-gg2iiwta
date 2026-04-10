class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] +=1

        pairs = freq.items()

        sorted_pairs = sorted(pairs, key = lambda x:x[1], reverse = True)

        for key, value in sorted_pairs:
            return key
        