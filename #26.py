#26

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums2 empty list
        nums2 = []
        # pointer = 0
        p = 0
        # while loop to check if pointer < len(nums)
        while (p < len(nums)):
            # if nums[p] is in nums2
            if (nums[p] in nums2):
                # .remove nums[p] from nums
                nums.remove(nums[p])
            # else
            else:
                # if nums[p] not in nums2
                if (nums[p] not in nums2):
                    # .append to nums2
                    nums2.append(nums[p])
                    # p += 1
                    p += 1
        # return length nums2
        return len(nums2)
