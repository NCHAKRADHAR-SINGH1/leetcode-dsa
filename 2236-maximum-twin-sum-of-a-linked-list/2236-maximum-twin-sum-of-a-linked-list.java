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
    public int pairSum(ListNode head) {
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode currNode=head;
        while(currNode.next!=slow){
            currNode=currNode.next;
        }
        currNode.next=null;

        ListNode curr=slow;
        ListNode prev=null;
        ListNode temp;
        while(curr!=null){
            temp=curr.next;
            curr.next=prev;
            prev=curr;
            curr=temp;
        }
        ListNode first=head;
        ListNode second=prev;
        int max_sum=0;
        while(second!=null){
          int  curr_sum=first.val+second.val;
          if (curr_sum > max_sum){
            max_sum=curr_sum;
          }
          first=first.next;
          second=second.next;
        }
        return max_sum;
        
    }
}