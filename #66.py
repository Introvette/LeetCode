class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse the list
        digits = digits[::-1]

        # initialize carry and pointer
        # 1 because only need to increment by 1, and 0 for the starting index
        one, i = 1, 0

        # continue to iterate while one == 1
        while one:
            # if i is still in bound
            if i < len(digits):
                # if digits i position is at an integer 9
                if digits[i] == 9:
                    # if it is 9 we're going to reset  pointer back to 0
                    digits[i] = 0
                # if not 9
                else:
                    # increment by 1
                    digits[i] += 1
                    # no longer need a carry so change one back to 0
                    one = 0
            # if i is not in bound we've reached the end
            else:
                digits.append(1)
                # don't have a carry so reset one to 0
                one = 0
            # increment i
            i += 1
        # return the array re-reversed
        return digits[::-1]
