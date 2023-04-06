class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # initialize first and last index as variables left & right
        left, right = 0, len(nums)
        # while loop to keep the search within the array
        while left < right:
            # initialize middle variable as average of left and right
            middle = (left + right) // 2
            # condition to make sure that target <= number at middle index
            if target <= nums[middle]:
                # the right side is now the middle index
                right = middle
            else:
                # if target is greater than the middle then middle = the left side not including the middle index
                left = middle + 1
        return left
