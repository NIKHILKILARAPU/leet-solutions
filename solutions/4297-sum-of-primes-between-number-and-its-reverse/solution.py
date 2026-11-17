class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        temp = n
        rev = 0
        while temp:
            digit = temp%10
            rev = (rev*10)+digit
            temp = temp//10
        minn,maxx=min(n,rev),max(n,rev)
        is_prime = [True]*(maxx+1)
        is_prime[0] = False
        is_prime[1] = False
        p = 2
        while p*p<=maxx:
            if is_prime[p]:
                for i in range(p*p,maxx+1,p):
                    is_prime[i] = False
            p = p+1
        summ = 0    
        for i in range(minn,maxx+1):
            if  is_prime[i]:
                summ = summ+i
        return summ                  

