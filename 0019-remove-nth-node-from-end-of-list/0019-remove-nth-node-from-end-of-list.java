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
    public ListNode removeNthFromEnd(ListNode head, int n) {
      ListNode dummy=new  ListNode(0);
      dummy.next=head;
      ListNode temp=head;
      int count=0;
      while(temp!=null){
        count++;
        temp=temp.next;
      }
      int res=count-n;
      ListNode curr=dummy;;
      while(res > 0){
        curr=curr.next;
        res--;
      }
      curr.next=curr.next.next;
      return dummy.next;
        
    }
}