# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head.next
        while fast :
            value=math.gcd(slow.val,fast.val)
            node=ListNode(value)
            slow.next=node
            node.next=fast
            slow=fast
            fast=fast.next
        return head
