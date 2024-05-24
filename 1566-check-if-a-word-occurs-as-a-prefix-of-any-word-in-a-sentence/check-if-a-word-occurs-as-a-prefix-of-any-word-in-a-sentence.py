class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        new_str=sentence.split()
        for string in new_str:
            if string.startswith(searchWord):
                res=new_str.index(string)
                return res+1
        return -1
        