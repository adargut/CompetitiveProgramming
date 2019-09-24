package robots;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {
	static Boolean possible = false;
	public static Optional<String> longest_string(List<String> robotStrings) {
	    Optional<String> longest = robotStrings.stream()
	            .sorted((e1, e2) -> e1.length() > e2.length() ? -1 : 1)
	            .findFirst();
	    return longest;
	}
	
	public static char nextMove (String robotMoves) {
		String distinct = robotMoves.chars().distinct().mapToObj(c -> 
		String.valueOf((char)c)).collect(Collectors.joining());
		if (distinct.length() == 3) 
			return 'B';
		if (distinct.contains("S") && distinct.contains("R"))
			return 'R';
		if (distinct.contains("S") && distinct.contains("P"))
			return 'S';
		if (distinct.contains("R") && distinct.contains("P"))
			return 'P';
		if (distinct.contains("R")) {
			Solution.possible = true;
			return 'P';
		}
		if (distinct.contains("S")) {
			Solution.possible = true;
			return 'R';
		}
		if (distinct.contains("P")) {
			Solution.possible = true;
			return 'S';
		}
		return ' ';
	} // EOF
	
	public static void main (String [] args) {
		Scanner scan = new Scanner(System.in);
		int T = scan.nextInt();
		for (int i = 1; i <= T; i++) {
			int st = 0;
			Solution.possible = false;
			String res = "";
			String robotString = "";
			int A = scan.nextInt();
			
			List <String> robots = new ArrayList<String>();
			for (int k = 0; k < A; k++) {
				robots.add(scan.next());
			} // fill in array of robot programs
			int longest = longest_string(robots).get().length();
			
			for (int ind = 0; ind < longest; ind++) {
				for (String program : robots) {
					robotString += program.charAt((ind % program.length()));
				}
			}
			
			int k = A;
			while (k <= robotString.length() ) {
				char nextMove = nextMove(robotString.substring(st,k));
				if (nextMove == 'B') { // bad move 
					break;
				}
				res += nextMove;
				st = k;
				k += A;
			}
			
			if (possible) {
				System.out.println("Case #" + i + ": " + res);
			}
			else {
				System.out.println("Case #" + i + ": " + "IMPOSSIBLE");
			}
			
		} // end of test case
	}
} // end of Solution
