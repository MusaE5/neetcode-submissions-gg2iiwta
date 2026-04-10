class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sums = 0
        ops = []
        for i in range(len(operations)):
            if operations[i] not in {'D', 'C', '+'}:
                ops.append(int(operations[i]))
            elif operations[i] == '+':
                ops.append(ops[-1] + ops[-2])
            elif operations[i] == 'D':
                ops.append(ops[-1] *2)  
            else:
                ops.pop()

        for j in range(len(ops)):
            sums+= ops[j]
        return sums    

                         

        