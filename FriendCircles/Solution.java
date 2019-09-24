// LeetCode #547 - Friend Circles
// The idea is to solve the problem using BFS algorithm
// Time complexity: O(E+V). Space complexity: O(E+V).

class Solution {
    public static int findCircleNum(int[][] M) {
    	int circles = 0;
    	int totalVertices = M.length;
    	
    	int [] visited = M[0];
    	for (int i = 0; i < visited.length; i++) {
    		visited[i] = 0;
    	}
    	
    	Queue<Integer> vertexQueue = new ArrayDeque<>();
    	vertexQueue.add(0);
    	totalVertices--;
    	visited[0] = 1;
    	
    	BFS:
    	while (totalVertices != 0) {
    		int currVertex = vertexQueue.remove();
    		for (int j = 0; j < visited.length; j++) {
    			if (visited[j] == 0 && (M[j][currVertex] == 1 || M[currVertex][j] == 1)) {
    				vertexQueue.add(j);
    				visited[j] = 1;
    				totalVertices--;
    			}
    		}
    		if (vertexQueue.size() == 0) {
    			for (int k = 0; k < visited.length; k++) {
    				if (visited[k] == 0) {
    					vertexQueue.add(k);
    					totalVertices--;
    					visited[k] = 1;
    					circles++;
    					continue BFS;
    				}
    			}
    		}
    	} // Finished iterating queue
    	return ++circles;
    }
}
