class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) -1
        l = 0
        result = []

        while l<r:
            if numbers[r] + numbers[l] > target:
                r-=1
            elif numbers[r] + numbers[l] < target:
                l+=1
            else:
                result.append(l+1)
                result.append(r+1)
                return result   


        