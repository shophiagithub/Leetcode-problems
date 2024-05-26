class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        new_p=paragraph.lower().split()
        punctuation="!.,;?'"
        for punc in punctuation:
            if punc in paragraph:
                paragraph=paragraph.replace(punc," ")
        new_p=paragraph.lower().split()
        c=0
        for words in new_p:
            if words not in banned and new_p.count(words)>c:
                c=new_p.count(words)
                word=words
        return word

        
        
        