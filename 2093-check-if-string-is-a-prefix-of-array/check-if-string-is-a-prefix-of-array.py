class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        empty=""
        for i in words:
            empty=empty+i
            if empty==s:
                return True
        return False    
        
        