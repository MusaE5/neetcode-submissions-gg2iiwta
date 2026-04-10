class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1

        pairs = hashmap.items()

        sorted_pairs = sorted(pairs, key = lambda x:x[1], reverse = True)
        top_k = sorted_pairs[:k]

        for n in top_k:
            result.append(n[0])

        return result   


