class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sk = []
        for i in operations:
            if i == 'C':
                sk.pop()
            elif i == 'D':
                sk.append(sk[-1]*2)
            elif i == '+':
                sk.append(sk[-1]+sk[-2])
            else:
                sk.append(int(i))
        return sum(sk)