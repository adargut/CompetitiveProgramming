public class LeetUT {

    public static void UnitTest() {
        Solution sol = new Solution();
        ListNode head = new ListNode(1);
        ListNode copy = head;
        int k = 10;

        // Create list of size k with successive numbers
        for (int i = 2; i <= k; i++) {
            copy.next = new ListNode(i);
            copy = copy.next;
        }

        // Test out print list
        Solution.printList(head);

        // Transform list
        sol.oddEvenList(head);

        System.out.println(System.lineSeparator());
        // Print transformed list
        Solution.printList(head);
    }
}
