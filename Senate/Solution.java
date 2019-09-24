package CodeJam;
import java.util.*;
import java.io.*;

public class Solution {
	
public static int GCD(int a, int b) { return b==0 ? a : GCD(b, a%b); }


 // input is sorted primes and number
 public static int[] Crack(int n, List < Integer > primes) { 
	 int [] res = new int[2];
	 int end = primes.size();
	 int start = 0;
	 while (primes.get(start) * primes.get(end - 1) != n) {
		 if (primes.get(start) * primes.get(end - 1) > n) 
			 end--;
		 else 
			 start++;
	 }
	 res[1] = primes.get(start);
	 res[0] = primes.get(end-1);
	 return res;
 }

 public static List < Integer > primesList(int n) { // method to get primes in range
  List < Integer > primes = new ArrayList < Integer > (); // list to store primes
  //loop through the numbers one by one
  for (int i = 2; i <= n; i++) {
   boolean isPrimeNumber = true;

   // check to see if the number is prime
   for (int j = 2; j < i; j++) {
    if (i % j == 0) {
     isPrimeNumber = false;
     break; // exit the inner for loop
    }
   }
   if (isPrimeNumber)
    primes.add(i); // prime found, add to list
  }
  Collections.sort(primes);
  return primes;
 }
 public static void main(String[] args) {
  int test = 5;
  int test1 = test++;
  int test2 = 5;
  System.out.println(test1 + test2);
  Scanner in = new Scanner(System.in);
  int T = in .nextInt(); // get # of tests
  for (int i = 1; i <= T; i++) {
	  String res = "";
	  // data structures used for question below
	  Map <Integer, String> dictionary = new HashMap<Integer,String>();
	  List <Integer> primesUsed = new ArrayList<>();
	  Map <Integer, Integer> factors = new HashMap<Integer, Integer>(); // map factors
   int num = in .nextInt(); // get N
   List <Integer> allPrimes = primesList(num);
   int length = in .nextInt(); // get L
   int [] hiddenText = new int[length];
   for (int k = 0; k < length; k++) { // iterate the length
	   hiddenText[k] = in .nextInt(); 
   };
   for (int m = 0; m < length - 1; m++) { 
	   int myGcd = GCD(hiddenText[m], hiddenText[m+1]);
	   factors.put(m + 1, myGcd);
   }
   
   //handle first number edge case
   int crack1 = Crack(hiddenText[0], allPrimes)[0];
   int crack2 = Crack(hiddenText[0], allPrimes)[1];
   int edge1 = GCD(hiddenText[0], hiddenText[1]) == crack1 ? crack2 : crack1;
   factors.put(0, edge1);
   
   //handle last number edge case
   crack1 = Crack(hiddenText[length-1], allPrimes)[0];
   crack2 = Crack(hiddenText[length-1], allPrimes)[1];
   edge1 = GCD(hiddenText[length-1], hiddenText[length-2]) == crack1 ? crack1 : crack2;
   factors.put(length-1, edge1);
   edge1 = GCD(hiddenText[length-1], hiddenText[length-2]) == crack1 ? crack2 : crack1;
   factors.put(length, edge1);
   
   primesUsed.addAll(factors.values());
   Set<Integer> set = new HashSet<>(primesUsed);
   primesUsed.clear();
   primesUsed.addAll(set);
   Collections.sort(primesUsed);
   char ch = 'A';
   for (Integer prime : primesUsed) { // iterate primes used to translate them
	   String letter = "";
	   letter += ch;
	   dictionary.put(prime, letter);
	   ch = (char)(ch + 1);
   }
   for (Integer factor : factors.keySet()) { 
	   res += dictionary.get(factors.get(factor));  
   }
   System.out.println(primesUsed);
   String message = "Case #" + i + ": " + res;
   System.out.println(message);
  } in .close();
 }
}