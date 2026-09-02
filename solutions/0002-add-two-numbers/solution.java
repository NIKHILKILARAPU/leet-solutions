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

        ListNode h1 = l1;
        ListNode h2 = l2;

        ListNode temp = new ListNode(0);
        ListNode head = temp;

        int carry = 0;

        while (h1 != null || h2 != null || carry != 0) {

            int x = (h1 != null) ? h1.val : 0;
            int y = (h2 != null) ? h2.val : 0;

            int sum = x + y + carry;

            carry = sum / 10;

            temp.next = new ListNode(sum % 10);
            temp = temp.next;

            if (h1 != null)
                h1 = h1.next;

            if (h2 != null)
                h2 = h2.next;
        }

        return head.next;
    }
}

