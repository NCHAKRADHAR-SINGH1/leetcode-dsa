class Solution(object):
    def isBalanced(self, num):
       even=[ int(num[i])  for i in range(len(num)) if (i)% 2==0]
       odd=[int(num[i]) for i in range(len(num)) if i % 2 !=0]
       return sum(even)==sum(odd)