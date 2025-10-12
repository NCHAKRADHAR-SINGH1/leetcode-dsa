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
    public ListNode swapNodes(ListNode head, int k) {
       int size=0;
       ListNode curr=head;
       while(curr!=null){
          size++;
          curr=curr.next;
       }
       int arr[]=new int[size];
       curr=head;
       int i=0;
       while(curr!=null){
         arr[i]=curr.val;
         curr=curr.next;
         i++;
       }
       int startIndex=k-1;
       int lastIndex=size-k;
       int temp=arr[startIndex];
       arr[startIndex]=arr[lastIndex];
       arr[lastIndex]=temp;
       ListNode currNode=null;
       ListNode tail=null;
       for(int num:arr){
         ListNode newNode=new ListNode(num);
         if(currNode==null){
            currNode=newNode;
            tail=newNode;
         }else{
            tail.next=newNode;
            tail=tail.next;
         }
        
       }
       return currNode;


    }

}