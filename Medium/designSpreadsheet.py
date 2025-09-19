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
