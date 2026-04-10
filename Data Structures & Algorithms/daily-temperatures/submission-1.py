class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                x = stack[-1]
                result[x] = i - stack.pop()
            stack.append(i)       
              
        return result        





                 

            


        

             

            


        