// LeetCode #328 - Odd Even List
// The idea is to shift every even node we encounter all the way to the end of the list, while maintaining required pointers
// Time complexity: O(n), where n is the size of the list. Space Complexity: O(1), beat 100% of Java submissions with memory usage

class Solution {
    public ListNode oddEvenList(ListNode head) {
        manipulateList(head);
        return head;
    }

    // Method to manipulate given list
    private void manipulateList(ListNode head) {
        // Save size of list
        int size = getSize(head);

        // Handle edge cases where we don't have to manipulate given list
        if (size == 0 || size == 1 || size == 2) return;

        // Locate tail of list
        ListNode tail = findTail(head);

        int k = 0;
        // Let the manipulation of the list begin
        while (k < size / 2) {
            ListNode tmp = head.next;
            head.next = head.next.next;
            head = head.next;

            moveNodeToEnd(tmp, tail);
            tail = tail.next;
            k++;
        }
    }

    // Utiliy method to locate tail of list
    private static ListNode findTail(ListNode head) {
        while (head.next != null) {
            head = head.next;
        }
        return head;
    }

    // Utility method to return size of list
    private static int getSize(ListNode head) {
        int size = 0;
        while (head != null) {
            size++;
            head = head.next;
        }
        return size;
    }

    // Utility method to move node to end of list
    private static void moveNodeToEnd(ListNode toMove, ListNode tail) {
        // Create copy of node to be moved
        int copy = toMove.val;

        // Move our desired node to end
        tail.next = new ListNode(toMove.val);
    }

    // Utility method to print list
    protected static void printList(ListNode node) {
        while (node != null) {
            System.out.print(node.val + "-");
            node = node.next;
        }
        System.out.print("NULL");
    }

    public static void main(String[] args) {
        LeetUT.UnitTest();
    }
    
} // End of solution
