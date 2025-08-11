class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def is_digit(s,k):
            list1=[]
            for i in range(0,len(s),k):
                list1.append(s[i:i+k])
            return list1
        def list_to_string(list1):
            final_result=""
            for i in range(len(list1)):
                li1=list1[i]
                li2=list(li1)
                target=0
                for ch in li2:
                    target=target+int(ch)
                final_result=final_result+str(target)
            return final_result
        while len(s) > k:
            li3=is_digit(s,k)
            s=list_to_string(li3)
        return s