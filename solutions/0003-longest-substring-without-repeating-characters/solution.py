class Solution(object):
    def lengthOfLongestSubstring(self, s):
        total_len = 0
        stri = ""
        
        for ele in s:
            if ele in stri:
                dup_index = stri.index(ele)
                stri = stri[dup_index + 1:]
                
            stri += ele
            total_len = max(total_len, len(stri))
            
        return total_len






         
