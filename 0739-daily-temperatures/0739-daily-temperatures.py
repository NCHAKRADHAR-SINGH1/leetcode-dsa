class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for i,value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
               previous_index=stack.pop()
               answer[previous_index]=i-previous_index
            stack.append(i)
        return answer