class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize our pointer
        p = 0
        # while p < length of nums
        while (p < len(nums)):
                # if current number is val:
                if nums[p] == val:
                    # remove it from nums
                    nums.pop(p)
                # else
                else:
                    # increment p by 1 to the next index
                    p += 1
        # return length of nums
        return len(nums)
