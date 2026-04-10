class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse = []
        for i in range(len(s)):
            reverse.append(s[i])

        for i in range(len(s)):
            s[i] = reverse.pop()   


        