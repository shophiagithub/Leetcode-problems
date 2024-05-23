class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
       
        ind=word.find(ch)
        sent=word[:(ind+1)]
        new_word=sent[::-1]
        next=word[(ind+1):]
        return new_word+next


