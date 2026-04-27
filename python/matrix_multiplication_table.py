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

    def print_to_html(self):
        html = "<table border='1'>\n"
        html += "<tr><th></th>"
        for j in range(1, len(self.dimensions)):
            html += F"<th>{self.titles[j]}</th>"
        html += "</tr>\n"
        for i in range(1, len(self.dimensions)):
            html += F"<tr><th>{self.titles[i]}</th>"
            for j in range(1, len(self.dimensions)):
                cell = self.table[i][j]
                if cell is None:
                    cell_str = ""
                else:
                    cell_str = F"{cell}"
                html += F"<td>{cell_str}</td>"
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


