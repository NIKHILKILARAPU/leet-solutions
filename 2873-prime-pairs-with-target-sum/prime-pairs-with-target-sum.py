
class Solution(object):
    def findPrimePairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 1:
            return []

        is_prime = [True] * (n + 1)

        is_prime[0] = False
        is_prime[1] = False

        p = 2

        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False

            p += 1

        pair_list = []

        for i in range(2, n//2 + 1):
            j = n-i
            if is_prime[i] and is_prime[j]:
                pair_list.append([i,j])
            

        return pair_list
