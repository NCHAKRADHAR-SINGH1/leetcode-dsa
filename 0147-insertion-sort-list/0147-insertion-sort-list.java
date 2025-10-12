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
    public ListNode insertionSortList(ListNode head) {
        ListNode curr=head;
        int size=0;
        while(curr!=null){
            size++;
            curr=curr.next;
        }
        int array[]=new int[size];
        curr=head;
        int i=0;
        while(curr!=null){
           array[i]=curr.val;
           curr=curr.next;
           i++;
        }
        int n=array.length;
        for( i=1;i<n;i++){
           int  key=array[i];
           int  j=i-1;
           while(j>=0 && array[j] > key){
              array[j+1]=array[j];
              j--;
           }
           array[j+1]=key;
        }
        ListNode headNode=null;
        ListNode tailNode=null;
        for(int num:array){
            ListNode newNode=new ListNode(num);
            if(headNode==null){
                headNode=newNode;
                tailNode=newNode;
            }else{
                tailNode.next=newNode;
                tailNode=tailNode.next;
            }
        }
        return headNode;

        
    }
}