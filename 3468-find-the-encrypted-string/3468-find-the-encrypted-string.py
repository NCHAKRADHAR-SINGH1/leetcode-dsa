class Solution(object):
    def getEncryptedString(self, s, k):
        final_string=""
        for i in range(len(s)):
            final_string=final_string+s[(i+k)% len(s)]
        return final_string

        