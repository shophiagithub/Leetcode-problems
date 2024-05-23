class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count=0
        for strs in words:
            if strs.find(pref)==0:
                count=count+1
        return count