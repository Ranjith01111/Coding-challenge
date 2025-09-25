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
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode nextAddress = head;
        ListNode ans=null;
        while(current != null){
            nextAddress = current.next;
            current.next = ans;
            ans = current;
            current = nextAddress;
        }
        return ans;
    }
}