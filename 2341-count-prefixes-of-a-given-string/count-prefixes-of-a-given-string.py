class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count=0
        for string in words:
            if s.startswith(string):
                count=count+1
        return count
        