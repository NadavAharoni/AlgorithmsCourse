from table2d import Table2D

recursive_lcs_counter=0
recursive_lcs_memo_counter = 0

def recursive_lcs_list(x : list, y: list):
    lcs = []
    global recursive_lcs_counter
    recursive_lcs_counter += 1
    if len(x)==0 or len(y)==0:
        return lcs
    last_x = x[-1]
    last_y = y[-1]
    if last_x == last_y:
        lcs = recursive_lcs_list(x[0:-1], y[0:-1])
        lcs += [ last_x ] 
    else:
        lcs1 = recursive_lcs_list(x[0:-1],y)
        lcs2 = recursive_lcs_list(x,y[0:-1])
        if len(lcs1) >= len(lcs2):
            lcs = lcs1
        else:
            lcs = lcs2
    return lcs

class CallGraph:
    def __init__(self):
        self._call_id = 0
        self.edges = []   # (parent_id, child_id, color)
        self.labels = []  # (node_id, label_str)

    def _new_node(self, x: str, y: str) -> int:
        my_id = self._call_id
        self._call_id += 1
        self.labels.append((my_id, f"#{my_id}\\nx='{x}'\\ny='{y}'"))
        return my_id

    def write_dot(self, filename="lcs_calls.dot"):
        with open(filename, "w") as f:
            f.write("digraph LCS {\n")
            f.write("  node [shape=box];\n")
            for node_id, label in self.labels:
                f.write(f'  {node_id} [label="{label}"];\n')
            for parent, child, color in self.edges:
                f.write(f'  {parent} -> {child} [color="{color}"];\n')
            f.write("}\n")


def recursive_lcs_str(x: str, y: str, graph: CallGraph = None, _parent=None, _edge_color="black") -> str:
    my_id = None
    if graph is not None:
        my_id = graph._new_node(x, y)
        if _parent is not None:
            graph.edges.append((_parent, my_id, _edge_color))
    if len(x) == 0 or len(y) == 0:
        return ""
    if x[-1] == y[-1]:
        return recursive_lcs_str(x[:-1], y[:-1], graph, my_id, "green") + x[-1]
    lcs1 = recursive_lcs_str(x[:-1], y, graph, my_id, "blue")
    lcs2 = recursive_lcs_str(x, y[:-1], graph, my_id, "red")
    return lcs1 if len(lcs1) >= len(lcs2) else lcs2

def recursive_lcs_memo(x : list, y: list, m : Table2D):
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
        # instead we use lcs + [last_x] which creates a new list
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


def recursive_lcs_memo_2(x : list, y: list, m : Table2D):
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
    X = "ABCBDAB"
    Y = "BDCABA"
    print(X)
    print(Y)

    g = CallGraph()
    recursive_lcs_str(X, Y, g)
    g.write_dot()

    if False:
        X=['A', 'B', 'C', 'B', 'D', 'A', 'B']
        Y=['B', 'D', 'C', 'A', 'B', 'A']
        print(X)
        print(Y)

        global recursive_lcs_counter
        recursive_lcs_counter = 0
        lcs = recursive_lcs_list(X, Y)
        print(F"result={lcs}")
        print(F"recursive_lcs_counter={recursive_lcs_counter}")

        global recursive_lcs_memo_counter
        recursive_lcs_memo_counter=0
        memo = Table2D()
        lcs = recursive_lcs_memo(X, Y, memo)
        print(F"result={lcs}")
        print(F"recursive_lcs_memo_counter={recursive_lcs_memo_counter}")


        # X = ['A', 'B', 'C']
        # Y = ['B', 'D', 'C']
        global recursive_lcs_memo_counter_2
        recursive_lcs_memo_counter_2=0
        memo_2 = Table2D(len(Y)+1, len(X)+1)
        lcs = recursive_lcs_memo_2(X, Y, memo_2)
        print(F"result={lcs}")
        print(F"recursive_lcs_memo_counter={recursive_lcs_memo_counter_2}")

        # ======== print results ========
        Y = [' '] + Y
        X = [' '] + X
        # fill the table with zeros
        for row_idx in range(len(Y)):
            for column_idx in range(len(X)):
                if not memo_2[row_idx, column_idx]:
                    memo_2[row_idx, column_idx] = MemoCell(0, ' ')

        # print the sequence X as column headers
        print("   ", end='')
        for column_idx in range(len(X)):
            print(F"{X[column_idx]}   |", end='')
        print()

        # print the rows of the table
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