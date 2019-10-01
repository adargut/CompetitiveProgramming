package manhattan;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
	
	public static void initiateMat (int [][]mat) {
		for (int i = 0; i < mat.length; i++) {
			for (int j = 0; j < mat[0].length; j++) {
				mat[i][j] = 0;
			}
		}
	}
	
	public static int [] bestLocation (int [][] mat) {
		int [] point = {0, 0};
		int max = 0;
		int x = 0;
		int y = 0;
		for (int i = 0; i < mat.length; i++) {
			for (int j = 0; j < mat.length; j++) {
				x = i;
				y = j;
				if (mat[i][j] > max) {
					max = mat[i][j];
					point[0] = x;
					point[1] = y;
				}
				if (mat[i][j] == max) {
					if (x < point[0]) 
					{
						max = mat[i][j];
						point[0] = x;
						point[1] = y;
					}
					if (point[0] == x) {
						if (y < point[1]) {
							max = mat[i][j];
							point[0] = x;
							point[1] = y;
						}
					}
				}
			}
		}
		return point;
	}
	
	public static void updateMat(int[][] mat, int posX, int posY, char dir) {
		switch (dir) {
		case 'N':
			for (int i = posY + 1; i < mat[0].length; i++) {
				for (int j = 0; j < mat.length; j++) {
				mat[j][i]++; }
			}
			break;
		case 'S':
			for (int i = posY - 1; i >= 0; i--) {
				for (int j = 0; j < mat.length; j++) { 
				mat[j][i]++; 
				}
			}
			break;
		case 'E':
			for (int i = posX + 1; i < mat[0].length; i++) {
				for (int j = 0; j < mat.length; j++) { 
				mat[i][j]++; }
			}
			break;
		case 'W':
			for (int i = posX - 1; i >= 0; i--) {
				for (int j = 0; j < mat.length; j++) { 
				mat[i][j]++;
				}
			}
			break;
		} // end of switch case
	}
	
	public static void main(String[]args) {
		String s = new String();
		System.out.println(s.length());
		  Scanner in = new Scanner(System.in);
		  int T = in .nextInt(); // get # of tests
		  for (int i = 1; i <= T; i++) { // foreach test in test set 
			  int P = in.nextInt();
			  int Q = in.nextInt();
			  int [][] mat = new int [Q+1][Q+1];
			  initiateMat(mat); // initiate the mat
			  for (int k = 1; k <= P; k++) {
				  int xPos = in.nextInt();
				  int yPos = in.nextInt();
				  char direction = in.next().charAt(0);
				  updateMat(mat, xPos, yPos, direction);
			  }
			  int [] location = bestLocation(mat);
			  System.out.println("Case #" + i + ": " +location[0] + " " + location[1]);
		  } // end of test case
	}
}
