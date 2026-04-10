class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        hashSet = set()

        for email in emails:
            s = email.split('@') 
            thisEmail = []

            for c in s[0]:
                if c != '.' and c!= '+':
                    thisEmail.append(c)
                elif c == "+":
                    break

            thisEmail.append('@')        

            for c in s[1]:
                thisEmail.append(c)
    
            
            hashSet.add(''.join(thisEmail))

        return  len(hashSet)               


        