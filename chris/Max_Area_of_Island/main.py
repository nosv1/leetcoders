# from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


class Position:
    def __init__(self, row: int, col: int) -> None:
        self._row: int = row
        self._col: int = col

    # def __eq__(self, other: Position) -> bool:
    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col

    # def move(self, direction: Position) -> None:
    def move(self, direction) -> None:
        self._row += direction.row
        self._col += direction.col


class Cell:
    def __init__(self, position: Position, cell_value: int) -> None:
        self._position = position
        self._cell_value: int = cell_value
        self._is_island: bool = self.is_island_check(cell_value)

    # def __eq__(self, other: Cell) -> bool:
    def __eq__(self, other) -> bool:
        return self.position == other.position

    def __hash__(self) -> int:
        return hash(self.position)

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
    def is_island_check(cell_value: int) -> bool:
        return True if cell_value == 1 else False


class Island:
    def __init__(self, cells: set[Cell]) -> None:
        self._cells: set(Cell) = cells

    @property
    def cells(self) -> set[Cell]:
        return self._cells

    @property
    def value(self) -> int:
        return sum([cell.cell_value for cell in self.cells])

    def add_cell(self, cell: Cell) -> None:
        self._cells.add(cell)


class Solution:
    # TODO: oooo what about multithreading and having many searchers instead of just one???

    searched_positions: set[Position] = {}
    islands: set[Island] = {}
    grid: list[list[int]] = []
    current_position: Position = None

    @dataclass
    class Direction:
        UP = Position(-1, 0)
        DOWN = Position(1, 0)
        LEFT = Position(0, -1)
        RIGHT = Position(0, 1)

        directions = {"UP": UP, "DOWN": DOWN, "LEFT": LEFT, "RIGHT": RIGHT}

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

    def check_surroundings(self, position: Position, island: Island) -> None:
        for direction in Solution.Direction.directions.values():
            new_position = Position(position.row, position.col)
            new_position.move(direction)
            if not self.position_in_grid(self.grid, new_position):
                continue

            island = self.check_position(new_position, island)

        return island

    def check_position(self, position: Position, island: Island) -> Island:
        if position in self.searched_positions:
            return island

        self.searched_positions.add(position)

        cell_value = self.cell_value(self.grid, position)
        cell = Cell(position, cell_value)
        if not cell.is_island:
            return island

        island.add_cell(cell)

        island = self.check_surroundings(position, island)
        return island

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.searched_positions = set()
        self.islands = set()
        # the idea is search a row of the grid at a time
        # looking left and right as we go throug the row
        # if we find a peice of an island, visit the cell and look around again, facing the way we were giong before we visited the cell (forward)

        start_row: int = 1 if len(grid) > 1 else 0
        start_col: int = 0
        self.current_position: Position = Position(start_row, start_col)

        largest_island: Island = Island(cells=set())

        for i, row in enumerate(grid):
            for j, cell_value in enumerate(row):
                position: Position = Position(i, j)
                island = Island(cells=set())
                island = self.check_position(position, island)
                if island.cells:
                    self.islands.add(island)

                    if island.value > largest_island.value:
                        largest_island = island

        if not self.islands:
            return 0

        return largest_island.value


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
    print(Solution().maxAreaOfIsland(grid=grid))
    grid: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0]]
    print(Solution().maxAreaOfIsland(grid=grid))
