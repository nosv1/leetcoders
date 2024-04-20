from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pass


if __name__ == "__main__":
    root = [1, 2, 3, None, 5]
    root = TreeNode(
        val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right=TreeNode(val=3)
    )
    assert root == ["1->2->5", "1->3"]
