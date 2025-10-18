# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        for i in nums:
            seen.add(i)
        dummy=ListNode(-1)
        dummy.next=head
        curr=dummy
        while curr  and  curr.next:
            if curr.next.val in seen:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next
    