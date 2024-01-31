import sys
from table2d import Table2D

def enumerate_parentheses(m):
    if len(m) <= 1:
        return m
    if len(m) <= 2:
        return [ m ]
    # else
    p1_x_p2 = []
    for k in range(1, len(m)):
        # print(F"k={k}, {m[:k]}, {m[k:]}")
        paren1 = enumerate_parentheses(m[:k])
        paren2 = enumerate_parentheses(m[k:])
        # print(F"k={k}: paren1={paren1}, paren2={paren2},")
        for p1 in paren1:
            for p2 in paren2:
                p1_x_p2.append([p1,p2])
    return p1_x_p2

def paren_str(m) -> str:
    if type(m) is not list:
        return m
    elif len(m) == 1:
        return F"{paren_str(m[0])}"
    elif len(m) == 2:
        return F"({paren_str(m[0])}*{paren_str(m[1])})"
    assert(len(m) <= 2)
    # following line is to prevent type errors
    return ""


class ChainOrderCell:
    def __init__(self, k, cost):
        self.k = k
        self.cost = cost

    def __repr__(self) -> str:
        return F"{self.k:2}: {self.cost:6}"

def matrix_chain_order(dimentions):
    n = len(dimentions)
    table = Table2D(n,n,ChainOrderCell(0,0))
    for i in range(0,n):
        table[i,i] = ChainOrderCell(0,0)

    for chain_length in range(2,n):
        print(F"chain_length={chain_length}")
        for start_idx in range(1, n - chain_length + 1):
            end_idx = start_idx + chain_length - 1
            min_cost = sys.maxsize
            min_cost_k = 0
            for k in range(start_idx, end_idx):
                cost = table[start_idx, k].cost + table[k+1, end_idx].cost + dimentions[start_idx-1]*dimentions[k]*dimentions[end_idx]
                print(F"start_idx={start_idx}, end_idx={end_idx}, k={k}, cost={cost}")
                if cost < min_cost:
                    min_cost = cost
                    min_cost_k = k
            table[start_idx, end_idx] = ChainOrderCell(min_cost_k, min_cost)
    return table

def main():
    matrix_dimentions = [30, 35, 15, 5, 10, 20 , 25]
    # matrix_dimentions = [30, 35, 15, 5, 10]
    table = matrix_chain_order(matrix_dimentions)
    print(table)
    return
    matrices = [ F"A{i}" for i in range(1,6) ]
    print(F"matrices={matrices}")

    p = enumerate_parentheses(matrices)
    print("-----------------")
    print(p)
    i = 0
    for p1 in p:
        # print(F"p1={p1}")
        i += 1
        str = paren_str(p1)
        print(F"{i:2}: str= {str[1:-1]}  -  {p1}")

if __name__=='__main__':
    main()