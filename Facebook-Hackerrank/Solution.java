class Solution {

    // Utility function for elements of arrays
    private static int minimumMoves(String Andrea, String Maria) {
        int res = 0;

        for (int curr = 0; curr < Andrea.length(); curr++) {
            int andreaDigit = Andrea.charAt(curr);
            int mariaDigit = Maria.charAt(curr);

            int diff = Math.abs(mariaDigit - andreaDigit);
            res += diff;
        }
        return res;
    } // EOF

    // Solver function
    public static int minimumMoves(int[] a, int[] m) {
        // Handle edge case for empty arrays
        if (a.length == 0 || m.length == 0) return 0;

        // Initial number of moves is 0
        int minMoves = 0;

        for (int pos = 0; pos < a.length; pos++) {
            String currAndrea = Integer.toString(a[pos]);
            String currMaria = Integer.toString(m[pos]);

            // Calculate separately minimum moves for Andrea and Maria's current integer
            minMoves += minimumMoves(currAndrea, currMaria);
        }
        return minMoves;
    } // EOF

    public static void main (String[] args) {
        UnitTest.RunTest();
    }
} // End of class
