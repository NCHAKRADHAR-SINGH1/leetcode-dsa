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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null||head.next==null||k==0){
            return head;
        }
        int length=1;
        ListNode tail=head;
        while(tail.next!=null){
            length++;
            tail=tail.next;     //moving tail to last node
        } 
        if(k % length==0){
           return head;
        }
        k=k % length;
        tail.next=head;    //pointing last node to first node like cll
        int count1=length-k;
        int count2=1;
        ListNode temp=head;
        while(count2 < count1){
            count2++;
            temp=temp.next;
        }
        ListNode newHead=temp.next;
        temp.next=null;
        return newHead;
  


    }
}