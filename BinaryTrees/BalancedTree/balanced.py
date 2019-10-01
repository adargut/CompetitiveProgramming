# """
# Balanced Binary Tree Problelm: check if tree is balanced.
# Notice that a tree is balanced iff |depth[root.left] - depth[root.right]| < 2, so we check for that.
# Time Complexity: O(n), where n:=#nodes.
# """
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        #  tree.isBalanced() iff |depth[root.left] - depth[root.right]| < 2
        return abs(self.nodeDepth(node=root.left) - self.nodeDepth(node=root.right)) in [0, 1]

    def nodeDepth(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self.nodeDepth(node.right), self.nodeDepth(node.left)) + 1


def main():
    sol = Solution()

    # """
    # Tree structure:
    #   3
    #  / \
    # 9  20
    #    / \
    #   15  7
    # """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    assert sol.isBalanced(root) is True

    # """
    # Tree structure:
    #       1
    #      / \
    #     2   2
    #    / \
    #   3   3
    #  / \
    # 4   4
    # """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    assert sol.isBalanced(root) is False


if __name__ == '__main__':
    main()
