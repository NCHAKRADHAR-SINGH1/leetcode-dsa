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
    public ListNode oddEvenList(ListNode head) {
        int i=1;
        ListNode odd=new ListNode();
        ListNode even=new ListNode();
        ListNode oddNode=odd;
        ListNode evenNode=even;
        ListNode curr=head;
        while(curr!=null){
            if(i % 2!=0){
                oddNode.next=curr;
                oddNode=oddNode.next;
            }else{
                evenNode.next=curr;
                evenNode=evenNode.next;
            }
            curr=curr.next;
            i++;
        }
        oddNode.next=even.next;
        evenNode.next=null;
        return odd.next;
    }
}