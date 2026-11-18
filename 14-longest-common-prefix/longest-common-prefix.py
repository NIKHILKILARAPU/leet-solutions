class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        max_str = min(strs, key=len)

        long_pre = ""
        index = 0

        for i in max_str:
            strs_count = 0

            for stri in strs:
                if len(stri) > index and stri[index] == i:
                    strs_count += 1

            if strs_count == len(strs):
                long_pre += i
                index += 1
            else:
                break

        return long_pre