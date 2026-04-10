class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for num in nums:
            if num>= target:
                return 1

        counter = 0

        for num in nums:
            counter +=num
        if counter< target:
            return 0 
        #edge cases               

        l, r = 0, 1
        min_length = 100001
        current_sum = nums[l] + nums[r]
        
        while r<len(nums):
            if r!= len(nums) -1 and current_sum<target:
                while r< len(nums)-1 and current_sum < target:
                    r+=1
                    current_sum+= nums[r]
            elif current_sum>=target:
                min_length = min(min_length, r-l+1) 
                current_sum -=nums[l]
                l+=1
            elif r-l ==1 and r<len(nums)-1:
                min_length = min(min_length, r-l+1) 
                current_sum -= nums[l]
                r+=1
                l+=1
                current_sum +=nums[r]   

            elif r-l > 1 and r == len(nums)-1 and current_sum>= target:
                min_length = min(min_length, r-l+1) 
                while l < r and current_sum >= target:
                    current_sum -= nums[l]
                    l+=1
                    min_length = min(min_length, r-l+1)
                return min_length
            else:
                return min_length        

             
            
        return min_length    
            
        
