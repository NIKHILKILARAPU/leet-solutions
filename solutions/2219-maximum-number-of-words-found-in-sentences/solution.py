class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for i in sentences:
            words = i.split()
            max_words =max(len(words),max_words)
        return max_words    

        
