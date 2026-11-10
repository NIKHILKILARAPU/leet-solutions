class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        count=0
        while(temp):
            digit=temp%10
            if(num%digit==0):
                count= count+1
            temp=temp//10
        return count        
        