public class UnitTest {

    public static void RunTest() {
        // Test case 1
        int[] Andrea = {1234, 4321};
        int[] Maria = {2345, 3214};
        int res = Solution.minimumMoves(Andrea, Maria);
        System.out.println("Result is: " + res + ". Expeceted: 10.");

        // Test case 2
        int[] Andrea2 = {123,543};
        int [] Maria2 = {321,279};
        res = Solution.minimumMoves(Andrea2, Maria2);
        System.out.println("Result is: " + res + ". Expeceted: 16.");

        // Test case 3
        int[] Andrea3 = {691554, 16423844};
        int [] Maria3 = {101717, 19427845};
        res = Solution.minimumMoves(Andrea3, Maria3);
        System.out.println("Result is: " + res + ". Expeceted: 31.");

        // Test case 4
        int[] Andrea4 = {666555,4};
        int [] Maria4 = {553009,8};
        res = Solution.minimumMoves(Andrea4, Maria4);
        System.out.println("Result is: " + res + ". Expeceted: 23.");

        // Test case 5
        int[] Andrea5 = {10, 20};
        int [] Maria5 = {67, 45};
        res = Solution.minimumMoves(Andrea5, Maria5);
        System.out.println("Result is: " + res + ". Expeceted: 19.");

        // Test case 6
        int[] Andrea6 = {55555, 66666};
        int [] Maria6 = {19410, 59520};
        res = Solution.minimumMoves(Andrea6, Maria6);
        System.out.println("Result is: " + res + ". Expeceted: 33.");

        // Test case 7
        int[] Andrea7 = {9999,9};
        int [] Maria7 = {8694,0};
        res = Solution.minimumMoves(Andrea7, Maria7);
        System.out.println("Result is: " + res + ". Expeceted: 18.");

        // Test case 8
        int[] Andrea8 = {444105666,4928};
        int [] Maria8 = {724049564,9695};
        res = Solution.minimumMoves(Andrea8, Maria8);
        System.out.println("Result is: " + res + ". Expeceted: 35.");

        // Test case 9
        int[] Andrea9 = {};
        int [] Maria9 = {};
        res = Solution.minimumMoves(Andrea9, Maria9);
        System.out.println("Result is: " + res + ". Expeceted: 0.");
    }
}
