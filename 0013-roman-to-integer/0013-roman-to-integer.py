class Solution:
    def romanToInt(self, s: str) -> int:
        ro_to_in = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        tot = 0
        m = len(s)
        for i in range(m):
            current_val = ro_to_in[s[i]]
            if i+1 < m and ro_to_in[s[i+1]] > current_val:
                tot -= current_val
            else:
                tot += current_val
        return tot

        