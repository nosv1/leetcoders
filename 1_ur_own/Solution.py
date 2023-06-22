class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        # isistance makes sure nums is a list
        if not isinstance(nums, list):
            return False
        
        # if nums is empty (nums = []) it returns False, otherwise True
        # so we check to make sure it's not empty here
        if not nums:
            return False

        # given we're tryna find duplicates, we can use a `set`` to store the numbers as we loop through them
        # we also use a set, because it takes O(1) time to check if a number is in a set, just magic storage (idk how it works)
        # if we were to use a list instead, it would take O(n) time to check if a number is in a list, 
        # basically the 'in' process would loop the list again
        unique_nums: set(int) = set()
        for n in nums:  # loop through the numbers, O(n) time
            if n in unique_nums:  # there exists a duplicate, checked in O(1) time
                return True  # return True if there exists a duplicate
            unique_nums.add(n)  # add the number to the set, O(1) time
        return False  # no duplicates found, return False