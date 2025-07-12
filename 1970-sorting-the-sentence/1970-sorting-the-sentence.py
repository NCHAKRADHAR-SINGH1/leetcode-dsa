class Solution:
    def sortSentence(self, s: str) -> str: 
        s=s.split()
        x=[]
        y=[]
        for i in range(len(s)):
            b=s[i]
            number=''.join(c for c in b if c.isdigit())
            x.append(int(number))
            string=''.join((d for d in b if d.isalpha()))
            y.append(string)
        z=list(zip(x,y))
        z.sort()
        result=' ' .join([sentence for number,sentence in z])
        return (result)