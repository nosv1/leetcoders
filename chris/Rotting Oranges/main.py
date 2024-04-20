# https://leetcode.com/problems/rotting-oranges/

from typing import List


class Orange:
    FRESH_ORANGE: int = 1
    ROTTEN_ORANGE: int = 2

    def __init__(self, value: bool, x: int, y: int) -> None:
        self.value = value
        self.rotten = self.is_rotten(self.value)
        self.x = x
        self.y = y

    @staticmethod
    def is_rotten(value: int) -> bool:
        return value == Orange.ROTTEN_ORANGE


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                self.grid[y][x] = Orange(grid[y][x], y, x)
        self.grid: List[List[Orange]]

        self.oranges_to_rot: List[Orange] = []
        self.simulate_rotting()

        return 0

    def print_grid(self) -> None:
        for row in self.grid:
            for orange in row:
                print(orange.value, end=" ")
            print()

    def rot_surrounding_oranges(self, orange: Orange) -> None:
        moves = [
            (-1, 0),  # down
            (0, -1),  # left
            (1, 0),  # up
            (0, 1),  # right
        ]

        for dy, dx in moves:
            new_y = orange.y + dy
            new_x = orange.x + dx

            # if one of the moves results in a negative index
            if not new_y + 1 or not new_x + 1:
                continue
            # if one of the moevs is greater than the bounds
            if new_y > len(self.grid) or new_x > len(self.grid[0]):
                continue

            orange_to_update = self.grid[orange.y + dy][orange.x + dx]
            self.oranges_to_rot.append(orange_to_update)

    def simulate_rotting(self) -> None:
        row_start = 0
        row_start_adjustment = -1
        for i in range(len(self.grid)):
            row_start_adjustment *= -1
            row_start += row_start_adjustment
            for j in range(row_start, len(self.grid[i]), 2):
                self.print_grid()
                input()
                orange = self.grid[i][j]
                if orange.rotten:
                    self.rot_surrounding_oranges(orange)

            for orange in self.oranges_to_rot:
                orange.value = Orange.ROTTEN_ORANGE


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]  # 4
    print(Solution().orangesRotting(grid))

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]  # -1
    print(Solution().orangesRotting(grid))

    grid = [[0, 2]]  # 0
    print(Solution().orangesRotting(grid))
