class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to string
        y = str(x)
        # set a variable to equal the string reversed
        z = y[::-1]
        # compare the original string to the new string
        if y == z:
        # if it's a match return True
            return True
