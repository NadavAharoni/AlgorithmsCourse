recursive_lcs_counter=0
recursive_lcs_memo_counter = 0

def recursive_lcs(x : list, y: list):
    lcs = []
    global recursive_lcs_counter
    recursive_lcs_counter += 1
    if len(x)==0 or len(y)==0:
        return lcs
    last_x = x[-1]
    last_y = y[-1]
    if last_x == last_y:
        lcs = recursive_lcs(x[0:-1], y[0:-1])
        lcs += [ last_x ] 
    else:
        lcs1 = recursive_lcs(x[0:-1],y)
        lcs2 = recursive_lcs(x,y[0:-1])
        if len(lcs1) >= len(lcs2):
            lcs = lcs1
        else:
            lcs = lcs2
    return lcs

class Matrix2D:
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
        for i in self.m:
            ret += F"{line_num}:"
            for j in i:
                ret += F"{j}, "
            ret += "\n"
            line_num += 1
        return ret


def recursive_lcs_memo(x : list, y: list, m : Matrix2D):
    global recursive_lcs_memo_counter
    recursive_lcs_memo_counter += 1
    # check if we already know the lcs for [len(x), len(y)]
    len_x = len(x)
    len_y = len(y)
    if m[len_x, len_y] is not None:
        lcs = m[len_x, len_y]
        return lcs

    if len(x)==0 or len(y)==0:
        m[len_x, len_y] = []
        return []
    
    last_x = x[-1]
    last_y = y[-1]
    if last_x == last_y:
        lcs = recursive_lcs_memo(x[0:-1], y[0:-1], m)
        # note: in the next line, if we use lcs.append(last_x) then lcs itself
        # is changed which is a bug, since lcs is returned from the martix
        # and we end up changing another entry in the matrix
        lcs = lcs + [last_x]
        m[len_x, len_y] = lcs
        return lcs
    else:
        lcs1 = recursive_lcs_memo(x[0:-1], y, m)
        lcs2 = recursive_lcs_memo(x, y[0:-1], m)
        if len(lcs1) >= len(lcs2):
            m[len_x, len_y] = lcs1
            return lcs1
        else:
            m[len_x, len_y] = lcs2
            return lcs2


class MemoCell:
    def __init__(self, length : int, arrow: str):
        self.length = length
        self.arrow = arrow

    def __str__(self):
        return F"{self.length, self.arrow}"


def recursive_lcs_memo_2(x : list, y: list, m : Matrix2D):
    global recursive_lcs_memo_counter_2
    recursive_lcs_memo_counter_2 += 1
    # check if we already know the lcs for [len(x), len(y)]

    len_x = len(x)
    len_y = len(y)
    if m[len_y, len_x] is not None:
        memo_cell = m[len_y, len_x]
        return memo_cell

    if len(x)==0 or len(y)==0:
        m[len_y, len_x] = MemoCell(0,' ')
        return m[len_y, len_x]
    
    last_x = x[-1]
    last_y = y[-1]
    if last_x == last_y:
        memo_cell = recursive_lcs_memo_2(x[0:-1], y[0:-1], m)
        new_memo_cell = MemoCell(memo_cell.length+1, "↖")
        # print(F"inserting {new_memo_cell} in {len_y},{len_x}")
        m[len_y, len_x] = new_memo_cell
        return m[len_y, len_x]
    else:
        memo_cell_1 = recursive_lcs_memo_2(x[0:-1], y, m)
        memo_cell_2 = recursive_lcs_memo_2(x, y[0:-1], m)
        if memo_cell_1.length >= memo_cell_2.length:
            m[len_y, len_x] = MemoCell(memo_cell_1.length, "←")
            return m[len_y, len_x]
        else:
            m[len_y, len_x] = MemoCell(memo_cell_2.length, "↑")
            return m[len_y, len_x]




def main():
    X=['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y=['B', 'D', 'C', 'A', 'B', 'A']
    print(X)
    print(Y)

    global recursive_lcs_counter
    recursive_lcs_counter = 0
    lcs = recursive_lcs(X, Y)
    print(F"result={lcs}")
    print(F"recursive_lcs_counter={recursive_lcs_counter}")

    global recursive_lcs_memo_counter
    recursive_lcs_memo_counter=0
    memo = Matrix2D()
    lcs = recursive_lcs_memo(X, Y, memo)
    print(F"result={lcs}")
    print(F"recursive_lcs_memo_counter={recursive_lcs_memo_counter}")


    # X = ['A', 'B', 'C']
    # Y = ['B', 'D', 'C']
    global recursive_lcs_memo_counter_2
    recursive_lcs_memo_counter_2=0
    memo_2 = Matrix2D(len(Y)+1, len(X)+1)
    lcs = recursive_lcs_memo_2(X, Y, memo_2)
    print(F"result={lcs}")
    print(F"recursive_lcs_memo_counter={recursive_lcs_memo_counter_2}")

    # ======== print results ========
    Y = [' '] + Y
    X = [' '] + X
    for row_idx in range(len(Y)):
        for column_idx in range(len(X)):
            if not memo_2[row_idx, column_idx]:
                memo_2[row_idx, column_idx] = MemoCell(0, ' ')
    print("   ", end='')
    for column_idx in range(len(X)):
        print(F"{X[column_idx]}   |", end='')
    print()
    for row_idx in range(len(Y)):
        print(F"   ", end='')
        for column_idx in range(len(X)):
            print(F"----|", end='')
        print()        
        print(F"{Y[row_idx]}: ", end='')
        for column_idx in range(len(X)):
            print(F"{memo_2[row_idx, column_idx].length}   |", end='')
        print()
        print(F"   ", end='')
        for column_idx in range(len(X)):
            print(F"   {memo_2[row_idx, column_idx].arrow}|", end='')
        print()        

    # print("===============")
    # print(memo_2)

    

if __name__=='__main__':
    main()