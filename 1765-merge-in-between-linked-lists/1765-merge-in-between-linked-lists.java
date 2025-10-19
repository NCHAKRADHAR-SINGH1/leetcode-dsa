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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
         ListNode temp=list1;
         ListNode lastNode;
         while(b > 0){
            temp=temp.next;
            b--;
         }
         lastNode=temp.next;
         ListNode currNode=list2;
         while(currNode.next!=null){
            currNode=currNode.next;
         }
         currNode.next=lastNode;
         ListNode curr=list1;
         int count=1;
         ListNode firstNode;
         while(count!=a){
            curr=curr.next;
            count++;
         }
         curr.next=list2;
         return list1;


      
        }
    }
