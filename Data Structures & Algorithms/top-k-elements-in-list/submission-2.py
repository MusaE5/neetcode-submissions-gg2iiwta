class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        top_k_list = []


        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1

        pairs = freq.items()

        sorted_pairs = sorted(pairs, key = lambda x:x[1], reverse = True)
        top_k = sorted_pairs[0:k]

        for key, value in top_k:
            top_k_list.append(key)

        return top_k_list    






        




        