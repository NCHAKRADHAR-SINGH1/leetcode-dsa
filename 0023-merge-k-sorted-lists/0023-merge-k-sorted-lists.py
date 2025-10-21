# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        arr=[]
        for head in lists:
         
            while head:
                arr.append(head.val)
                head=head.next
        def merge_sort(arr):
            if len(arr) <=1:
                return arr
            mid=len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            return merge(left,right)
        def merge(left,right):
            result=[]
            i=0
            j=0
            while i<len(left) and j <len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        final_result=merge_sort(arr)
        head=None
        tail=None
        dummy=ListNode()
        for i in final_result:
            node=ListNode(i)
            if head is None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=tail.next
        return head



            