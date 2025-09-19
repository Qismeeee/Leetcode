class Spreadsheet(object):

    def __init__(self, rows):
        self.rows = rows
        self.grid = {}  # key: (col_index, row_index) -> value

    def _cell_key(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return (col, row)

    def _term_value(self, term):
        if term[0].isdigit():
            return int(term)
        key = self._cell_key(term)
        return self.grid.get(key, 0)

    def setCell(self, cell, value):
        key = self._cell_key(cell)
        self.grid[key] = value

    def resetCell(self, cell):
        key = self._cell_key(cell)
        if key in self.grid:
            del self.grid[key]

    def getValue(self, formula):
        expr = formula[1:]
        x, y = expr.split('+')
        return self._term_value(x) + self._term_value(y)


def run_tests():
    ss = Spreadsheet(3)
    assert ss.getValue("=5+7") == 12
    ss.setCell("A1", 10)
    assert ss.getValue("=A1+6") == 16
    ss.setCell("B2", 15)
    assert ss.getValue("=A1+B2") == 25
    ss.resetCell("A1")
    assert ss.getValue("=A1+B2") == 15
    print("case1 ok")

    ss = Spreadsheet(5)
    assert ss.getValue("=0+0") == 0
    ss.setCell("Z5", 100)
    assert ss.getValue("=Z5+1") == 101
    ss.setCell("C3", 7)
    ss.setCell("C3", 9)
    assert ss.getValue("=C3+Z5") == 109
    ss.resetCell("Z5")
    assert ss.getValue("=C3+Z5") == 9
    print("case2 ok")

    ss = Spreadsheet(2)
    ss.setCell("A1", 1)
    ss.setCell("B1", 2)
    ss.setCell("C1", 3)
    assert ss.getValue("=A1+B1") == 3
    assert ss.getValue("=B1+C1") == 5
    assert ss.getValue("=9+1") == 10
    print("case3 ok")

run_tests()
