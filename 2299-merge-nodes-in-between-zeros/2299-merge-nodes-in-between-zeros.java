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
        ListNode dummy=head.next;
        ListNode modify=dummy;
        while(modify!=null){
            int sum=0;
            while(modify.val!=0){
                sum += modify.val;
                modify=modify.next;
            }
            dummy.val=sum;
            modify=modify.next;
            dummy.next=modify;
            dummy=dummy.next;

        }
        return head.next;
    }
}