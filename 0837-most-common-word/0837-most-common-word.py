class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for p in "!?',;.":
           paragraph = paragraph.replace(p, " ")
        para=paragraph.split()
        para1=" ".join(i.lower().strip(" .,!") for i in para)
        para2=para1.split()
        dici={}
        for r in range(len(para2)):
           dici[para2[r]]=1+dici.get(para2[r],0)
        max_count=0
        most_frequency=""
        for key,value in dici.items():
             if key not in banned and value > max_count :
                max_count = value
                most_frequency=key
        return (most_frequency)
        