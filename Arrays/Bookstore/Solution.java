// Problem #1052 on LeetCode
// Time complexity: O(n)
// Space complexity: used 41.7 MB of memory, beat 100% of all Java submissions

class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        // Variables to be used
        int currUnsatisfied = 0;
        int maxUnsatisfied = Integer.MIN_VALUE;

        // Handle grumpyness
        int grumpyFrom = 0;
        int grumpyTo = X - 1;
        int maxFrom = 0;
        int maxTo = X - 1;

        // Initially we use ungrumpify from 0 to X
        for (int i = grumpyFrom; i < grumpyTo; i++) {
            if (grumpy[i] == 1) {
                currUnsatisfied += customers[i];
            }
        }
        maxUnsatisfied = currUnsatisfied;

        while (grumpyTo + 1 < customers.length) {
            if (grumpy[grumpyFrom] == 1) {
                currUnsatisfied -= customers[grumpyFrom];
            }

            // Shift segment to the right one bit
            grumpyFrom++;
            grumpyTo++;

            if (grumpy[grumpyTo] == 1) {
                currUnsatisfied += customers[grumpyTo];
            }

            // This is a better placement to use ungrumpify
            if (currUnsatisfied > maxUnsatisfied) {
                maxUnsatisfied = currUnsatisfied;
                maxFrom = grumpyFrom;
                maxTo = grumpyTo;
            }
        } // End of while

        int finalSum = 0;
        for (int i = 0; i < maxFrom; i++) {
            if (grumpy[i] == 0)
                finalSum += customers[i];
        }
        for (int i = maxFrom; i <= maxTo; i++) {
            finalSum += customers[i];
        }
        for (int i = maxTo + 1; i < customers.length; i++) {
            if (grumpy[i] == 0)
                finalSum += customers[i];
        }
        return finalSum;
    }
}
