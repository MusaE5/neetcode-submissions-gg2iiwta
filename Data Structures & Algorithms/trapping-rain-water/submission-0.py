class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_l = 0
        max_r = 0
        amount_water = 0
        
     

        while l<r:
            if height[l] < height[r]:
                max_l = max(max_l, height[l])
                amount_water += max_l - height[l]
                l+=1
                
                
            else:
                max_r = max(max_r, height[r])
                amount_water += max_r -height[r]
                r-=1

        return amount_water        
                

            









        