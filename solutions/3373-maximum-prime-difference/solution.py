class Solution(object):
    def maximumPrimeDifference(self, nums):

        prime_indices = []

        for i in range(len(nums)):
            count = 0

            if nums[i] > 1:
                for j in range(2, nums[i]):
                    if nums[i] % j == 0:
                        count += 1

                if count == 0:
                    prime_indices.append(i)

        if len(prime_indices) == 0:
            return 0

        return prime_indices[-1] - prime_indices[0]
