/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head==null){
            return head;
        }
        ListNode dummy=new ListNode(-1);
        dummy.next=head;
        ListNode prev=dummy;
        ListNode curr=head;
        ListNode nextNode=head.next;
        while(nextNode!=null){
           
           curr.next=nextNode.next;
           nextNode.next=curr;
           prev.next=nextNode;
           prev=curr;
           curr=curr.next;
           if (curr==null){
            break;
           }
           if(curr.next==null){
            break;
           }
          nextNode=curr.next;
        }
        return dummy.next;
    }
}