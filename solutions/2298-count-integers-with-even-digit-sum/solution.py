class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in range(1,num+1):
            temp = i
            summ=0
            while(temp):
                digit = temp%10
                summ = summ+digit
                temp = temp//10
            if(summ%2==0):
                count = count+1
        return count            

        
