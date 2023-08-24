from __future__ import annotations
from typing import List
from dataclasses import dataclass


class Position:
    def __init__(self, row: int, col: int) -> None:
        self._row: int = row
        self._col: int = col

    def __eq__(self, other: Position) -> bool:
        return self.row == other.row and self.col == other.col

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    def move(self, direction: Position) -> None:
        self._row += direction.row
        self._col += direction.col


class Cell:
    def __init__(self, position: Position, cell_value: int) -> None:
        self._position = position
        self._cell_value: int = cell_value
        self._is_island: bool = self.is_island(cell_value)

    def __eq__(self, other: Cell) -> bool:
        return self.position == other.position

    @property
    def position(self) -> Position:
        return self._position

    @property
    def cell_value(self) -> int:
        return self._cell_value

    @property
    def is_island(self) -> bool:
        return self._is_island

    @staticmethod
    def is_island(cell_value: int) -> bool:
        return True if cell_value == 1 else False


class Island:
    def __init__(self) -> None:
        self._cells: set(Cell) = set()

    @property
    def cells(self) -> set(Cell):
        return self._cells

    @property
    def value(self) -> int:
        return sum(lambda cell: cell.cell_value, self._cells)

    def add_cell(self, cell: Cell) -> None:
        self._cells.add(cell)


class Solution:
    # TODO: oooo what about multithreading and having many searchers instead of just one???

    searched_cells: set(Cell) = set()
    islands: set(Island) = set()
    grid: [list[int]] = []
    current_position: Position = None

    directions = {
        "UP": Position(-1, 0),
        "DOWN": Position(1, 0),
        "LEFT": Position(0, -1),
        "RIGHT": Position(0, 1),
    }

    @property
    def current_cell(self) -> Cell:
        return Cell(
            self.current_position, self.cell_value(self.grid, self.current_position)
        )

    @staticmethod
    def cell_value(grid: list[list[int]], position: Position) -> int:
        return grid[position.row][position.col]

    @staticmethod
    def position_in_grid(grid: list[list[int]], position: Position) -> bool:
        return (
            position.row >= 0
            and position.row < len(grid)
            and position.col >= 0
            and position.col < len(grid[0])
        )

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.grid = grid
        # the idea is search a row of the grid at a time
        # looking left and right as we go throug the row
        # if we find a peice of an island, visit the cell and look around again, facing the way we were giong before we visited the cell (forward)

        start_row: int = 1 if len(grid) > 1 else 0
        start_col: int = 0
        self.current_position: Position = Position(start_row, start_col)

        while True:
            break


if __name__ == "__main__":
    grid: list[list[int]] = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    Solution().maxAreaOfIsland(grid=grid)
