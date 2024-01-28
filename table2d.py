class Table2D:
    def __init__(self, rows: int = 0, columns : int = 0, value = None):
        self.m = []
        self.m.extend([[] for _ in range(rows)])
        for row in self.m:
            row.extend([value for _ in range(columns)])

    def check_extend(self, i, j):
        if len(self.m) <= i:
            num_extra_rows = i + 1 - len(self.m)
            self.m.extend([[] for _ in range(num_extra_rows)])
        row = self.m[i]
        if len(row) <= j:
            num_extra_columns = j + 1 - len(row)
            extra = [None for _ in range(num_extra_columns)]
            row.extend(extra)

    def __getitem__(self, ij : tuple):
        i = ij[0]
        j = ij[1]
        self.check_extend(i,j)
        return self.m[i][j]

    def __setitem__(self, ij : tuple, value):
        i = ij[0]
        j = ij[1]
        self.check_extend(i,j)
        self.m[i][j] = value

    def __str__(self) -> str:
        ret = ""
        line_num = 0
        for row in self.m:
            ret += F"{line_num}: | "
            ret += " | ".join([str(i) for i in row])
            ret += "\n"
            line_num += 1
        return ret