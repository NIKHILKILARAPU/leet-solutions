class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_sum = 0
        element_sum = 0
        
        for i in nums:
            element_sum = element_sum + i
            temp = i
            while(temp):
                digit = temp % 10
                digit_sum = digit_sum + digit
                temp = temp // 10
                
        return abs(element_sum - digit_sum)
