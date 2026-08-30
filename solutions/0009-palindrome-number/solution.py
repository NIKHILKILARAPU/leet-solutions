class Solution(object):
    def isPalindrome(self, x):
        test = str(x)
        return test== test[::-1]
