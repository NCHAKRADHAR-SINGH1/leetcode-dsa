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
        def merge_sort(arr):
            if len(arr) <=1:
                return arr
            mid=len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            return merge(left,right)
        def merge(left,right):
            result=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        result1=merge_sort(arr)
        dummy=None
        tail=None
        for i in result1:
            newNode=ListNode(i)
            if dummy is None: 
                dummy=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=tail.next
        return dummy



        