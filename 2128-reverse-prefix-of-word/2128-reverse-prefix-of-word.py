class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
    
        idx = word.index(ch)
        return word[idx::-1] + word[idx+1:]
        
        