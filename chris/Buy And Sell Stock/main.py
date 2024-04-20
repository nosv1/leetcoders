from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0

        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy

        return profit

        pot_buy = float("inf")
        pot_sell = float("-inf")
        pot_profit = lambda: pot_sell - pot_buy

        buy = float("inf")
        sell = float("-inf")
        profit = lambda: sell - buy

        for price in prices:
            if price < pot_buy:
                pot_buy = price
                continue

            if pot_buy != float("inf") and price - pot_buy > profit():
                pot_sell = price

                if pot_profit() > profit():
                    buy = pot_buy
                    sell = pot_sell
                    pot_sell = float("-inf")

        return profit() if profit() > 0 else 0


if __name__ == "__main__":
    prices = [5, 5, 4, 9, 3, 8, 5, 5, 1, 6, 8, 3, 4]
    assert Solution().maxProfit(prices) == 7

    prices = [7, 4, 1, 2]
    assert Solution().maxProfit(prices) == 1

    prices = [2, 1, 2, 1, 0, 1, 2]
    assert Solution().maxProfit(prices) == 2

    prices = [2, 4, 1]
    assert Solution().maxProfit(prices) == 2

    prices = [7, 1, 5, 3, 6, 4]
    assert Solution().maxProfit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0
