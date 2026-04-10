class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = arr[len(arr) -1]
        result = [0] * len(arr)
        

        for i in range(len(arr)-2, -1, -1):
            curMax = max(curMax, arr[i+1])
            result[i] = curMax

        result[-1] = -1    

        return result



        