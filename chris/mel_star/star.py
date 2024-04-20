from __future__ import annotations

"""
V = (m^k+1 - 1) / (m - 1)
Assign 1 as label to root
TArray[1][1] = 0
d = ((ceil(V) / 2) / (m - 1))
for each child of root j <- 2 to m
    TArray[1][j] = TArray[1][j-1] + d
    TArray[2][j] = TArray[1][j] + 1
TArray[1][1] = 1
TArray[2][1] = 2
Apply recursive call on 1 to m-1 sub-trees in 2nd level
    Edge-Weights will increase by 1 starting from 3

    Label of verticies will be TArray[j] <- Edge-Weight-TArray[Parent(j)]
    Avoid Edge-Weights that are already used in level 1
Apply recurse call on mth sub-tree in 2nd level
    Edge-Weights will decrease by 1 starting from V
    Label of verticies will be TArray[j] <- Edge-Weight-TArray[Parent(j)]
"""


class Node:
    def __init__(self, label: int, parent: Node) -> None:
        self.label = label
        self.parent = parent
        self.cost = parent.cost + 1
        self.children = []


class Graph:
    def __init__(self, num_branches, num_nodes) -> None:
        self.root: Node = Node(1)
        self.num_branches = num_branches
        self.num_nodes = num_nodes

        for i in range(num_branches):
            self.root.children.append(Node(i + 2))


if __name__ == "__main__":
    pass
