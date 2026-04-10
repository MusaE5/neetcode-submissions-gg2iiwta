class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        result = []
        product_suffix = 1
        product_prefix = 1

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                product_prefix *= nums[i-1]
                prefix.append(product_prefix)  

        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                suffix.append(1)
            else:
                product_suffix *= nums[i+1]
                suffix.insert(0,product_suffix)

        for i in range(len(nums)):
            result.append(suffix[i] * prefix[i])

        return result     






            

        