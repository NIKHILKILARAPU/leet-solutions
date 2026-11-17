class Solution(object):
    def maximumPrimeDifference(self, nums):

        first = -1
        last = -1

        for i in range(len(nums)):

            n = nums[i]
            prime = True

            if n < 2:
                prime = False
            else:
                for j in range(2, int(n ** 0.5) + 1):
                    if n % j == 0:
                        prime = False
                        break

            if prime:
                if first == -1:
                    first = i

                last = i

        if first == -1:
            return 0

        return last - first