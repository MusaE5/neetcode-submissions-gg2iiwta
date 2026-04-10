class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i +1
            r = len(nums) -1
            target = nums[i] * -1

            while l < r:
                if nums[l] + nums[r] < target:
                    l +=1
                    continue
                if nums[l] + nums[r] > target:
                    r -= 1
                    continue
                if nums[l] + nums[r] == target:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1   
        return triplets                    



        