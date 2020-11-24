class Blosum():

    # based on: https://gist.github.com/jwintersinger/1870047#file-blosum-py


    def __init__(self, matrix_file_path):
        self.Load(matrix_file_path)


    def Load(self, matrix_file_path):
        with open(matrix_file_path) as matrix_file:
            matrix = matrix_file.read()
        lines = matrix.strip().split('\n')
        header = lines.pop(0)
        columns = header.split()
        matrix = {}
        for row in lines:
            entries = row.split()
            row_name = entries.pop(0)
            matrix[row_name] = {}
            if len(entries) != len(columns):
                raise Exception('Improper entry number in row')
            for column_name in columns:
                matrix[row_name][column_name] = entries.pop(0)
        self.matrix = matrix


    def Lookup(self, a, b):
        a = a.upper()
        b = b.upper()
        if a not in self.matrix or b not in self.matrix[a]:
            raise Exception('Not found in matrix')
        return self.matrix[a][b]



