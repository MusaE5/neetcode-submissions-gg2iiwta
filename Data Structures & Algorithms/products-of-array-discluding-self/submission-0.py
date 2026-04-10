class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = []

        for i in range (len(nums)):
            if i == 0:
                product = 1
                l.append(product)
            else:
                product *= nums[i-1]
                l.append(product)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                product = 1
                r.insert(0, product)  
            else:
                product *= nums[i+1]
                r.insert(0, product)  

        results = []
        for i in range(len(nums)):
            answer = r[i] * l[i]
            results.append(answer)

        return results                            
            







