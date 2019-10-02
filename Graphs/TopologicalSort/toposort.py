from collections import defaultdict
from copy import deepcopy
from queue import Queue

import numpy as np


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def removeEdge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    def topoSort(self):
        visited = np.zeros(len(self.V), dtype=bool)  # initialize all nodes as unvisited
        stack = []

        for node in self.V:
            if not visited[node]:
                self.topoUtil(node=node, stack=stack, visited=visited)
        return stack

    def topoUtil(self, node, stack, visited):
        visited[node] = True  # mark node as visited
        neighbors = self.graph[node]

        for neighbor in neighbors:
            if not visited[neighbor]:
                self.topoUtil(neighbor, stack, visited)

        stack.insert(0, node)  # insert curr vertex after having consumed all vertices approachable from it

    def reverseGraph(self):
        vert = deepcopy(self.V)
        reverse = Graph(vert)
        reverse.graph = deepcopy(self.graph)

        for node in range(len(self.V)):
            neighbors = self.graph[node]
            while len(neighbors) > 0:
                neighbor = neighbors.pop()
                reverse.removeEdge(node, neighbor)
                reverse.addEdge(neighbor, node)
        return reverse

    # here we utilize topological sort to find longest path in graph
    def longestPath(self):
        sortedGraph = self.topoSort()
        reverseGraph = self.reverseGraph()
        dp, idx = np.zeros(len(sortedGraph)), 1
        maxDist = 0

        while idx < len(sortedGraph):
            node = sortedGraph[idx]
            if not reverseGraph.graph[node]:  # no entering nodes
                bestDist = 0
            else:
                bestDist = max(dp[neighbor] for neighbor in reverseGraph.graph[node]) + 1
            dp[node] = bestDist
            if bestDist > maxDist:
                maxDist = bestDist
            idx += 1
        return int(maxDist)


def main():
    passed = 0

    print("***FIRST TEST CASE***")
    g = Graph([0, 1, 2, 3, 4, 5, 6, 7])
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(7, 3)
    g.addEdge(2, 7)
    g.addEdge(6, 7)
    g.addEdge(4, 6)
    g.addEdge(4, 2)
    path = g.longestPath()
    err = "Expected: 6 Got: " + str(path)
    assert path == 6, err
    passed += 1
    print("PASSED")

    print("***SECOND TEST CASE***")
    g = Graph([0, 1, 2, 3])
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 3)
    path = g.longestPath()
    err = "Expected: 2 Got: " + str(path)
    assert path == 2, err
    passed += 1
    print("PASSED")

    print("***THIRD TEST CASE***")
    g = Graph([0, 1, 2, 3, 4])
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 4)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    path = g.longestPath()
    err = "Expected: 2 Got: " + str(path)
    assert path == 2, err
    passed += 1
    print("PASSED")

    print("***FOURTH TEST CASE***")
    g = Graph(np.arange(11))
    g.addEdge(9, 0)
    g.addEdge(0, 1)
    g.addEdge(1, 4)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(9, 10)
    g.addEdge(9, 2)
    g.addEdge(0, 2)
    path = g.longestPath()
    err = "Expected: 3 Got: " + str(path)
    assert path == 3, err
    passed += 1
    print("PASSED")

    msg = "Passed " + str(passed) + "/4 tests"
    print(msg)


if __name__ == '__main__':
    main()
