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
    public ListNode partition(ListNode head, int x) {
        ListNode left=new ListNode();
        ListNode right=new ListNode();
        ListNode lhead=left;
        ListNode rhead=right;
        ListNode curr=head;
        while(curr!=null){
           if(curr.val < x){
             lhead.next=curr;
             lhead=lhead.next;
           }else{
             rhead.next=curr;
             rhead=rhead.next;
           }
           curr=curr.next;
        }
        lhead.next=right.next;
        rhead.next=null;
        return left.next;
    }
}