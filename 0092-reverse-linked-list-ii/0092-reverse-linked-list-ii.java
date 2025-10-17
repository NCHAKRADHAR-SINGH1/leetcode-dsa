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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head.next==null){
            return head;
        }
        int length=1;
        ListNode tempNode=head;
        while(tempNode!=null){
            length++;
            tempNode=tempNode.next;
        }
        ListNode leftNode=head;
        ListNode rightNode=head;
        ListNode prevNode=null;
        ListNode firstNode;
        ListNode lastNode;
        int i=1;
        while(i < left){
            prevNode=leftNode;
            leftNode=leftNode.next;
            i++;
        }
        firstNode=leftNode;
        int j=1;
        while(j < right){
            rightNode=rightNode.next;
            j++;
        }
        lastNode=rightNode.next;
        ListNode prev=null;
        ListNode curr=leftNode;
        ListNode temp;
        while(curr!=lastNode){
            temp=curr.next;
            curr.next=prev;
            prev=curr;
            curr=temp;
        }
        if(prevNode!=null){
            prevNode.next=prev;
        }else{
            head=prev;
        }
        firstNode.next=lastNode;
        return head;
    
        


        
    }
}