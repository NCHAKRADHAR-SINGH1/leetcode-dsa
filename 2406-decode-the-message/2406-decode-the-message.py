class Solution(object):
    def decodeMessage(self, key, message):
        key=key.replace(" ","")
        li=[]
        for i in key:
         if i not in li:
            li.append(i)
        dici={}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(li)):
            s=li[i]
            s1=alphabet[i]
            dici[s]=s1
        decoded=""
        for ch in message:
            if ch==" ":
                decoded+=" "
            else:
                decoded+=dici[ch]
        return decoded    

