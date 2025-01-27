class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i,char in enumerate(shortest):
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
        return shortest