class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 1
        num = 0
        last = None
        last_last = 1
        while True:
            num += 1
            last_last = last
            last = num

            if count > n:
                return last_last

            count += 1

            if num % 5 == 0:
                continue
            elif num % 3 == 0:
                continue
            elif num % 2 == 0:
                continue


if __name__ == "__main__":
    ugly_number_10 = Solution().nthUglyNumber(10)
    assert ugly_number_10 == 12

    ugly_number_1 = Solution().nthUglyNumber(1)
    assert ugly_number_1 == 1
