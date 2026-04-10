class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for i in range(len(strs)):
            length = str(len(strs[i]))
            encode.append(length)
            encode.append('#')
            encode.append(strs[i])
        return ''.join(encode)    
        

    def decode(self, s: str) -> List[str]:
        decode = []
        l = 0
        while l<len(s):
            j=l
            while s[j].isdigit():
                j+=1
            length = int(s[l:j])
            j+=1
            decode.append(s[j:j+length])
            l = j+length

        return decode    



