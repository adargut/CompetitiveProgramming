# """
# LeetCode problem 913: Cat and Mouse
# The idea is to run BFS from mouse to every one of the neighbors of the hole node, namely target nodes.
# If there exists a target node s.t. the mouse is closer to it than the cat, determined by BFS, mouse wins.
# Otherwise, check if mouse can reach a cycle of length > 3 in the graph faster than cat, again using BFS.
# If mouse achieves that, it's a draw. Otherwise, cat wins.
# Time Complexity: O(n+m), where n:=#vertices and m:=#edges in graph.
# """
import numpy as np
import sys
from queue import Queue
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        targeted = graph[0]  # attempt to reach neighbor of hole
        mouse, cat, closestToMouse = 1, 2, -1
        mouseDist = sys.maxsize
        for target in targeted:  # mouse attempts to reach nearest neighbor of hole node
            currDist = self.doBFS(graph, mouse, target)
            if currDist < mouseDist:
                closestToMouse = target
                mouseDist = currDist
        catDist = self.doBFS(graph, cat, closestToMouse)
        if mouseDist < catDist:
            return 2  # mouse is closer to a neighbor of hole, therefore he wins

        cyclicNodes = []  # now figure out if draw or loss, compute distance of mouse from all cycles
        for node in range(len(graph)):
            currDist = self.doBFS(graph=graph, start=node, end=node)
            if currDist != sys.maxsize and currDist > 4:  # check if cycle found & is large enough
                cyclicNodes.append(True)
            else:
                cyclicNodes.append(False)
        # check if mouse can reach a cyclic node faster than cat, any cyclic node
        for node in range(len(graph)):
            if cyclicNodes[node]:
                mouseDist, catDist = self.doBFS(graph, mouse, node), self.doBFS(graph, cat, node)
                if mouseDist < catDist:
                    return 0  # mouse can reach cyclic node faster, so a draw occurs
        return 1  # cat wins

    # augmented version of BFS for this problem
    def doBFS(self, graph: List[List[int]], start: int, end: int):
        dist = 0
        visited = np.zeros(len(graph), dtype=bool)

        q = Queue()
        q.put(start)
        visited[start] = True
        while not q.empty():
            dist += 1
            node = q.get()  # pop head of queue
            if node == start and node == end and dist > 1:
                return dist
            for neighbor in graph[node]:
                if dist > 2 and neighbor == start:
                    dist += 1
                    return dist
                if not visited[neighbor]:
                    if neighbor == end and start != end:
                        return dist
                    visited[neighbor] = True
                    q.put(neighbor)
        return sys.maxsize


# basic UT
sol = Solution()
graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
res = sol.catMouseGame(graph=graph)
print(res)
