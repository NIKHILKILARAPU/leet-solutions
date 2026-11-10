class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_count=0
        for i in nums:
            temp = i
            count=0
            while(temp):
                digit = temp%10
                count = count+1
                temp=temp//10
            if count%2==0:
                even_count = even_count+1
        return even_count    