from typing import List
import numpy as np
from numpy import prod

# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product: int = 1
        for n in nums:
            if not n:
                total_product *= 
        products = []
        for i, n in enumerate(nums):

        return products


if __name__ == "__main__":
    output = Solution().productExceptSelf([1, 2, 3, 4])
    assert output == [24, 12, 8, 6]

    output = Solution().productExceptSelf([-1, 1, 0, -3, 3])
    assert output == [0, 0, 9, 0, 0]
