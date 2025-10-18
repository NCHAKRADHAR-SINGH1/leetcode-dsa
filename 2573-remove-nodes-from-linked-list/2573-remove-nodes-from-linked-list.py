# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curr=head
        while curr:
           arr.append(curr.val)
           curr=curr.next
        stack=[]
        for val in arr:
            while stack and stack[-1] < val:
                stack.pop()
            stack.append(val)
        head=None
        tail=None
        for i in stack:
            node=ListNode(i)
            if head is None:
              head=node
              tail=node
            else:
                tail.next=node
                tail=tail.next
        return head
        