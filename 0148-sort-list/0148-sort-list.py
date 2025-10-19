# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr.sort()
        dummy=None
        tail=None
        for i in arr:
            newNode=ListNode(i)
            if dummy is None: 
                dummy=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=tail.next
        return dummy



        