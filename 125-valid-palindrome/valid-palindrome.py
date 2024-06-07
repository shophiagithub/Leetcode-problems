class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #empty=" "
        if s==" ":
            return True
        punctuation=[',', ':', '!', '.', '?', ';', "'", '"', '(', ')', '[', ']', '{', '}', '-', '_', '@', '#', '$', '%', '^', '&', '*', '~', '`', '/', '\\']
        for punc in punctuation:
            if punc in s:
                s=s.replace(punc,"")
        new_s=s.replace(" ","").lower() 
        a=len(new_s)-1
        for i in range(len(new_s)): 
            if(new_s[i]!=new_s[a]):
                return False
            a-=1
        return True
        






        