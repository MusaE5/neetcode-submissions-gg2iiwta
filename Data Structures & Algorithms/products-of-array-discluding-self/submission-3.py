class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, suffix, products = [], [], []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                product = 1
            else:
                product*= nums[i-1]
                prefix.append(product)

        for n in range(len(nums)-1, -1, -1):
            if n == len(nums) -1:
                suffix.append(1)
                product = 1
            else:
                product*= nums[n+1]
                suffix.insert(0, product)

        for j in range(len(nums)):
            products.append(prefix[j]*suffix[j])

        return products            






        