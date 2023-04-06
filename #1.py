class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # pointer variable (p)
        p = 0
        # found = False
        found = False
        # for loop for num in range(0, len(nums))
        for i in range(0, len(nums)):
            # p = i
            p = i
            # if found
            if found:
                # break
                break
            # for a in range(0, len(nums))
            for a in range(0, len(nums)):
                # if nums i + nums a == target & i is not a
                if nums[p] + nums[a] == target and not i == a:
                    found = True
                    # return i, a
                    return i, a
                    # break
                    break
