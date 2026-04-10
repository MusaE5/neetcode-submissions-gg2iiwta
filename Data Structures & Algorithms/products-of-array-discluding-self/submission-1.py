class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        product = 0

        for i in range(len(nums)):
            if i == 0:
                product = 1
            else:
                product*= nums[i-1]

            prefix.append(product)

        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                product = 1

            else:
                product *= nums[i+1]

            suffix.insert(0, product)

        results = []

        for i in range(len(nums)):
            result = prefix[i] * suffix[i]
            results.append(result)

        return results                   


