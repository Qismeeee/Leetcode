class Solution(object):
    def solveSudoku(self, board):
        FULL = (1 << 9) - 1
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []
        digits = [chr(ord('1') + i) for i in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    empties.append((i, j))
                else:
                    b = (i // 3) * 3 + (j // 3)
                    m = 1 << (ord(c) - ord('1'))
                    rows[i] |= m
                    cols[j] |= m
                    boxes[b] |= m

        def popcount(x):
            cnt = 0
            while x:
                x &= x - 1
                cnt += 1
            return cnt

        def dfs():
            if not empties:
                return True
            best_idx = -1
            best_mask = 0
            best_cnt = 10
            for idx, (i, j) in enumerate(empties):
                b = (i // 3) * 3 + (j // 3)
                used = rows[i] | cols[j] | boxes[b]
                mask = FULL & ~used
                cnt = popcount(mask)
                if cnt == 0:
                    return False
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_idx = idx
                    best_mask = mask
                    if cnt == 1:
                        break
            i, j = empties.pop(best_idx)
            b = (i // 3) * 3 + (j // 3)
            mask = best_mask
            while mask:
                lb = mask & -mask
                d = lb.bit_length() - 1
                ch = digits[d]
                board[i][j] = ch
                rows[i] |= lb
                cols[j] |= lb
                boxes[b] |= lb
                if dfs():
                    return True
                rows[i] &= ~lb
                cols[j] &= ~lb
                boxes[b] &= ~lb
                mask -= lb
            board[i][j] = '.'
            empties.insert(best_idx, (i, j))
            return False

        dfs()

def run_tests():
    sol = Solution()
    puzzle = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]
    solved = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"],
    ]
    b1 = [row[:] for row in puzzle]
    sol.solveSudoku(b1)
    assert b1 == solved

    b2 = [row[:] for row in solved]
    b2[0][2] = "."
    sol.solveSudoku(b2)
    assert b2 == solved

    b3 = [row[:] for row in solved]
    sol.solveSudoku(b3)
    assert b3 == solved

    print("OK")

run_tests()
