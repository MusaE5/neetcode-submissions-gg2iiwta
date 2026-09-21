class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []

        if x in arr:
            index = arr.index(x)
        else:
            if arr[0] > x:
                index = 0
            elif arr[-1] < x:
                index = len(arr) -1
            else:
                prev_v = arr[0]
                for i, value in enumerate(arr):
                    if value> x and prev_v<x:
                        if abs(prev_v - x) < abs(value-x):
                            index = i-1
                        elif abs(prev_v - x) > abs(value-x):
                            index = i
                        else:
                            index = i-1
                        break
                    else:
                        prev_v = value
        result = []
        result.append(arr[index])
        l = index -1 if index-1 >=0 else None
        r = index +1 if index+1 <len(arr) else None
        while len(result) <k:
            if l is not None:
                if l<0:
                    l = None
                    
            if r is not None:
                if r>= len(arr):
                    r = None

            if l is None:
                result.append(arr[r])
                r+=1
            elif r is None:
                result.append(arr[l])
                l-=1
            else:
                if abs(x - arr[l]) < abs(x-arr[r]):
                    result.append(arr[l])
                    l-=1
                elif abs(x - arr[l]) > abs(x-arr[r]):
                    result.append(arr[r])
                    r+=1
                else:
                    result.append(arr[l])
                    l-=1
        return sorted(result)


        
                    
                    
            