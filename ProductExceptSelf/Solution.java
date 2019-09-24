// LeetCode #238 - Product of Array Except Self
// The idea is to perform two iterations: one going from left to right, then from right to left.
// During either iteration, update content of cell to be product of all cells to its right/left.
// Obtain the final result by multiplying the results of both iterations coordinate-wise
// Time complexity: O(n), beat 100% of Java submissions (1ms practical runtime). Space complexity: O(n).

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Init variables
        int[] output = new int[nums.length];
        output[1] = nums[0];

        // Perform first iteration: from left to right
        for (int i = 2; i < nums.length; i++) {
            output[i] = output[i-1] * nums[i-1];
        }

        int[] leftIter = new int[nums.length];
        leftIter[nums.length-1] = output[nums.length-1];
        leftIter[nums.length-2] = nums[nums.length-1];

        // Perform second iteration: from right to left
        for (int i = nums.length - 3; i >= 0; i--) {
            leftIter[i] = nums[i + 1] * leftIter[i + 1];
        }

        output[0] = leftIter[0];
        // Unify both iterations
        for (int i = 1; i < output.length - 1; i++) {
            output[i] *= leftIter[i];
        }
        return output;
    }
} // End of Solution
