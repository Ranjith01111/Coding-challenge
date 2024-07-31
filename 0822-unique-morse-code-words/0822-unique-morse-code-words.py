class Solution(object):
    def uniqueMorseRepresentations(self, words):

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        for word in words:
            transform = ''.join(morse[ord(c) - ord('a')] for c in word)
            trans.add(transform)
        return len(trans) 
        