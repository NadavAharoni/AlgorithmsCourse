class matrix_multiplication_table:
    def __init__(self,dimensions):
        self.dimensions = dimensions
        self.titles = {}
        for i in range(len(dimensions)-1):
            self.titles[i+1] = F"A{i+1}: ? x ?" # exercise: fill in the dimensions of the matrices
        
        self.table = {}
        for i in range(1, len(dimensions)):
            self.table[i] = {}
            for j in range(1, len(dimensions)):
                self.table[i][j] = None

    def cell_to_html(self, cell):
        if cell is None:
            return ""
        if type(cell) is not dict:
            return ""
        # else, cell is a dict
        ret = ""
        i,j = cell["range"]
        if j == i+1:
            ret += F"ops: A{i} x A{j}"
        else:
            ret += F"ops: A{i} .. A{j}"

        if "cost" in cell:
            ret += F"<br>cost: {cell['cost']}"
        if "optimized_parenthesization" in cell:
            ret += F"<br>optimized: {cell['optimized_parenthesization']}"
        return ret

    def print_to_html(self):
        html = "<table border='1' style='border-collapse: collapse'>\n"
        html += "<tr><th></th>"
        for j in range(1, len(self.dimensions)):
            html += F"<th>{self.titles[j]}</th>"
        html += "</tr>\n"
        for i in range(1, len(self.dimensions)):
            html += F"<tr><th>{self.titles[i]}</th>"
            for j in range(1, len(self.dimensions)):
                cell = self.table[i][j]
                html += F"<td>{self.cell_to_html(cell)}</td>"
            html += "</tr>\n"
        html += "</table>"
        return html

def main():
    dimensions=[50, 10, 25, 45, 8]
    t = matrix_multiplication_table(dimensions)

    output_file = "matrix_multiplication_table.html"
    with open(output_file, "w") as f:
        f.write(t.print_to_html())

if __name__ == "__main__":
    main()


