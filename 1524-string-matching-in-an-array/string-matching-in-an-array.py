class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words1=sorted(words,key=len)
        empty=[]
        for i in range(len(words1)):
            for j in range(i+1,len(words1)):
                if words1[i] in words1[j]:
                    empty.append(words1[i])
                    break
        return empty