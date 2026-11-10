class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ=0
        product=1
        while(n):
            digit = n%10
            summ=summ+digit
            product=product*digit
            n=n//10
        return product-summ    
        
