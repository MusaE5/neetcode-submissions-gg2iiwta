class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1

        pairs = hash.items()
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse= True)
        top_k_pairs = sorted_pairs[:k]

        results = []
        for pair in top_k_pairs:
            results.append(pair[0])
        return results                

