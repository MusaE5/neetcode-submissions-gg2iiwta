class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] +=1
        
        pairs = []

        for ke, v in seen.items():
            pairs.append((ke, v))
        
        pairs.sort(key = lambda x :x[1], reverse = True)

        result = []

        for i in range(k):
            result.append(pairs[i][0])
            
        return result
        