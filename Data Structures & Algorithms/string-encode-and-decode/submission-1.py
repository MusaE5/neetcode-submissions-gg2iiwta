class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for i in range(len(strs)):
            length = str(len(strs[i]))
            encode.append(length)
            encode.append(',')
            encode.append(strs[i])

        return ''.join(encode) 



    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i<len(s):
            j=i
            while s[j].isdigit():
                j+=1
            length = int(s[i:j])
            j+=1
            decode.append(s[j: j+length])
            i = j+length


        return decode        



