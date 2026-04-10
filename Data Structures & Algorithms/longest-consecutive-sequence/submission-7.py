class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_seq = 0

        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                seq = 1
                current_num = nums[i]
                while current_num + 1 in num_set:
                    seq+=1
                    current_num +=1
                max_seq = max(max_seq, seq)

        return max_seq            

        