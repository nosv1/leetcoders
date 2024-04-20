from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __str__(self):
        # not necessary, just making sure things do things
        vals: list[int] = [str(self.val)]
        list_node = self.next
        while list_node:
            vals.append(str(list_node.val))
            list_node = list_node.next
        return ", ".join(vals)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        return


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(head)
    # Solution().reorderList(head)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)
    # Solution().reorderList(head)
