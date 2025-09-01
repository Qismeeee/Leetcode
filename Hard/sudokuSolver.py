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
