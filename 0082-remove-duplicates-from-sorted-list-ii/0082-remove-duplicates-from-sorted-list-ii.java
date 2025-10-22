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
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null){
            return head;
        }
        ListNode dummy=new ListNode(0);
        dummy.next=head;
        ListNode prev=dummy;
        ListNode curr=head;
        ListNode nextNode=head.next;
        while( curr!=null && nextNode!=null){
           boolean is_equal=false;
           while(nextNode!=null && curr.val==nextNode.val){
               is_equal=true;
               nextNode=nextNode.next;
           }
           if(is_equal){
             prev.next=nextNode;
           }else{
             prev=prev.next;
           }
           curr=nextNode;
           if(nextNode!=null){
             nextNode=nextNode.next;
           }
        


        }
        return dummy.next;
       

        
    }
}