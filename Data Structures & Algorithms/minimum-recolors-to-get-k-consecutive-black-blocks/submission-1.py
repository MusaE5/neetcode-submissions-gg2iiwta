class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_oper = 101
        operations = 0
        r = 0
        while r<k:
            if blocks[r] == "W":
                operations +=1
            r+=1

        l=1       

        min_oper = min(min_oper, operations)


        while r<len(blocks):
            if blocks[l-1] == "W":
                operations -=1   
    
            if blocks[r] == "W":
                operations+=1  
        
            min_oper = min(min_oper, operations)
            l+=1
            r+=1 
        return min_oper               


        





        