package golfgophers;
import static java.util.Arrays.stream;

import java.util.*;

public class Solution {
	
	public static class CRT {

	    public static int chineseRemainder(int[] n, int[] a) {
	 
	        int prod = stream(n).reduce(1, (i, j) -> i * j);
	 
	        int p, sm = 0;
	        for (int i = 0; i < n.length; i++) {
	            p = prod / n[i];
	            sm += a[i] * mulInv(p, n[i]) * p;
	        }
	        return sm % prod;
	    }
	 
	    private static int mulInv(int a, int b) {
	        int b0 = b;
	        int x0 = 0;
	        int x1 = 1;
	 
	        if (b == 1)
	            return 1;
	 
	        while (a > 1) {
	            int q = a / b;
	            int amb = a % b;
	            a = b;
	            b = amb;
	            int xqx = x1 - q * x0;
	            x1 = x0;
	            x0 = xqx;
	        }
	 
	        if (x1 < 0)
	            x1 += b0;
	 
	        return x1;
	    }
	}
	
	public static void EighteenMills(int m) {
		String[]  blades = new String[18];
		for (int i = 0; i <= 17; i++) {
			blades[i] = String.valueOf(m); // set blades to 18
		}
		String res = Arrays.deepToString(blades);
		res = res.replace("[", "");
		res = res.replace("]", "");
		res = res.replace(",", "");
		System.out.println(res);
	}
	
	public static int [] JudgeRes() {
		Scanner sc = new Scanner(System.in);
		int []  judge = new int[18];
		for (int i = 0; i <= 17; i++) {
			judge[i] = sc.nextInt(); // set blades to 18
		}
		return judge;
	}
	
	public static void main (String[]args) {
		  Scanner in = new Scanner(System.in);
		  int T = in .nextInt(); // get # of tests
		  int N = in.nextInt(); // get # of nights
		  int M = in.nextInt(); // get # of max gophers
		  for (int i = 1; i <= T; i++) { // foreach test in test set 
			  
			  int guess = 0;
			  
			  for (int k = 0; k < 7; k++) { // guess 10 times
				  
			  Solution.EighteenMills(i); // use 18 blades always
			  int tmpguess = 0;
			  // get judge results
			  int [] judge = JudgeRes();
			  for (int j = 0; j <= 17; j++) {
				  tmpguess += judge[j];
			  }
			  if (tmpguess > guess) {
				  guess = tmpguess;
			  }
			  
			  } // end of 7 guesses
			  
			  System.out.println(guess);
			  int ret = in.nextInt();
			  if (ret != 1) {
				  System.exit(0);
			  }
		  	} // end test cases
		  in.close();
		  }
	}

