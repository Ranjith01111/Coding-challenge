class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0
    
        for word in words:
            if all(char in allowed_set for char in word):
                count += 1
    
        return count
        