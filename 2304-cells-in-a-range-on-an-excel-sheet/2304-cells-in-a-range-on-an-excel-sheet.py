class Solution(object):
    def cellsInRange(self, s):
        col1, row1, col2, row2 = s[0], s[1], s[3], s[4]
        cols = [chr(c) for c in range(ord(col1), ord(col2) + 1)]
        rows = [str(r) for r in range(int(row1), int(row2) + 1)]
        result = [c + r for c in cols for r in rows]
        return result
        