class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # loop through nums
        # for each number, subtract it from target
        # if the result is in nums, return the index of the current number and the index of the result
        # if the result is not in nums, continue
        # if the loop completes, return None
        
        nums_set: set(int) = set(nums)
        for i, n in enumerate(nums):
            looking_for: int = target - n
            if looking_for in nums_set:
                looking_for_index = nums.index(looking_for)
                if looking_for_index == i:
                    continue
                return [i, looking_for_index]
                