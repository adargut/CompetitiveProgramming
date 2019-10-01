package CodeJam;
import java.util.*;
import java.io.*;
@SuppressWarnings("unused")

public class Senate {	
	public static void main (String [] args ) {
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt(); // # of tests
		for (int i = 1; i <= T; i++) {
		String res = "";
		int N = scan.nextInt(); // scan # of parties
		int [] parties = new int[N];
		for (int j = 0; j < N; j++) {
			parties[j] = scan.nextInt();
		}
		Arrays.sort(parties);
		while (N > 0) {
			if (N >= 2 && parties[N-1] == parties[N-2]) {
				res += Character.toString((char) (N-1 + 65)) + 
						Character.toString((char) (N-2 + 65)) + " ";
				parties[N-1]--;
				parties[N-2]--;
			}
			else {
				res += Character.toString((char) (N-1 + 65)) + 
						Character.toString((char) (N-1 + 65)) + " ";
				parties[N-1]-=2;
			}
			if (N>= 1 && parties[N-1] == 0) {
				N--;
				if (N>=2 && parties[N-2] == 0) 
					N--;				
			}
		}
		System.out.println("Case #" + i + ": " + res);
		}
		scan.close();
	}
}