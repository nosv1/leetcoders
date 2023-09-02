# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

from math import ceil


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_2D_index(num_cols, index):
            row = index // num_cols

            if row == 0:
                col = index
            else:
                col = index % (row * num_cols)

            return row, col

        def binary_search(A, n, target):
            left = 0
            right = n - 1
            while left != right:
                middle = ceil((left + right) / 2)
                row, col = get_2D_index(len(A[0]), middle)
                if A[row][col] > target:
                    right = middle - 1
                else:
                    left = middle

            row, col = get_2D_index(len(A[0]), left)
            if A[row][col] == target:
                return True

            return False

        return binary_search(matrix, len(matrix) * len(matrix[0]), target)


if __name__ == "__main__":
    matrix = [[1, 3], [10, 11], [23]]
    target = 4
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1]]
    target = 0
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1, 3, 5]]
    target = 1
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1, 3]]
    target = 1
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1, 1]]
    target = 2
    print(Solution().searchMatrix(matrix, target))

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(Solution().searchMatrix(matrix, target))
