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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> st1=new Stack<Integer>();
        Stack<Integer> st2=new Stack<Integer>();
        ListNode temp1=l1;
        ListNode temp2=l2;
        while(temp1!=null){
            st1.push(temp1.val);
            temp1=temp1.next;
        }
        while(temp2!=null){
            st2.push(temp2.val);
            temp2=temp2.next;
        }
        ListNode dummy=new ListNode(-1);
        ListNode curr=dummy;
        int carry=0;
        while(!st1.isEmpty() || !st2.isEmpty()){
            int sum=carry;
            if(!st1.isEmpty()){
                sum=sum+st1.pop();
            }
            if(!st2.isEmpty()){
                sum=sum+st2.pop();
            }
            ListNode newNode=new ListNode(sum % 10);
            carry=sum / 10;
            curr.next=newNode;
            curr=curr.next;
        }
        if(carry!=0){
            ListNode node=new ListNode(carry);
            curr.next=node;
        }
       ListNode prev=null;
       ListNode currNode=dummy.next;
       ListNode temp;
       while(currNode!=null){
        temp=currNode.next;
        currNode.next=prev;
        prev=currNode;
        currNode=temp;
       }
       return prev;
    }
}