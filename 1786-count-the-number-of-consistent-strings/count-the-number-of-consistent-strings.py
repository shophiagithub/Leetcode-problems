class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed=set(allowed)
        count=0
        for word in words:
            for char in word:
                if char not in allowed:
                    count+=1
                    break
        return len(words)-count
        