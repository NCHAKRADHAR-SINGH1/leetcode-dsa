class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i=="C": #c removes the last digit
               stack.pop()
            elif i=='D': # d performs the double the previous value 
               stack.append(2*stack[-1])
            elif i=='+': # it performs the adding of two values
               stack.append(stack[-1]+stack[-2])
            else:
               stack.append(int(i))
        return (sum(stack[0:]))