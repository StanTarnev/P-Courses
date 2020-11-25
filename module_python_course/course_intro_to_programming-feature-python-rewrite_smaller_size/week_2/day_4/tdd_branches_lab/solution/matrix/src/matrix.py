class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = self.string_to_matrix(self.matrix_string)

    def string_to_matrix(self, matrix_string):
        matrix = []

        for string in matrix_string.split('\n'):
            row = []
            for item in string.split(' '):
                row.append(int(item))
            matrix.append(row)
        return matrix

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        matrix_column = []

        for row in self.matrix:
            matrix_column.append(row[index - 1])
        return matrix_column
