class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            x += 1 if op[1] == '+' else -1
        return x
