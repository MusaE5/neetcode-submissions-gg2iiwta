class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            alive = True

            while alive and stack and stack[-1] >0 and num<0:
                if abs(stack[-1]) < abs(num):
                    stack.pop()
                elif abs(stack[-1]) > abs(num):
                    alive = False
                elif abs(stack[-1]) == abs(num):
                    stack.pop()
                    alive = False
            if alive:
                stack.append(num)             
            

        
        
        return stack                








        