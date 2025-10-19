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
    public ListNode mergeNodes(ListNode head) {
        ListNode modify=head.next;
        ListNode temp=modify;
        int sum=0;
        while(temp!=null){
            if(temp.val==0){
                modify.val=sum;
                temp=temp.next;
                modify.next=temp;
                modify=modify.next;
                sum=0;
            }else{
            
              sum += temp.val;
              temp=temp.next;
            }
            
           

        }
        return head.next;
    }
}