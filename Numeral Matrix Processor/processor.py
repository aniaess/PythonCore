class Matrixes:

    def __init__(self):
        self.matrix_A = []
        self.matrix_B = []
        self.result = []
        self.cofactors =[]

    def draw_a_board(self):
        print("The result is:")
        for row in self.result:
            for col in row:
                if col == 0:
                    print(f"0 ", end="" )
                else:
                    print(f"{str(col)} ", end="")
            print()

    def input_matrix(self, optional="first "):
        matrix = []
        dimensions = [int(x) for x in input(f"Enter size of {optional}matrix: ").split(" ")]
        if dimensions == [1,1]:
            print(f"Enter {optional}matrix:")
            return [[int(input())]]
        else:
            print(f"Enter {optional}matrix:")
            for i in range(dimensions[0]):
                matrix.append([float(x) if "." in x else int(x) for x in input().split(" ")])
            return matrix

    def addindg(self):
        self.matrix_A = self.input_matrix()
        self.matrix_B = self.input_matrix("second ")
        if len(self.matrix_A[0]) == len(self.matrix_B[0]) and len(self.matrix_A[1]) == len(self.matrix_B[1]):
            for i in range(len(self.matrix_A)):
                self.result.append([])
                for j in range(len(self.matrix_A[0])):
                    self.result[i].append(int(self.matrix_A[i][j] * 100 + self.matrix_B[i][j] * 100) / 100)
            self.draw_a_board()
        else:
            print("The operation cannot be performed.")

    def multiply_by_constant(self, matrix, number):
        for i in range(len(matrix)):
            self.result.append([])
            for j in range(len(matrix[i])):
                self.result[i].append(number * matrix[i][j])
        self.draw_a_board()

    def multiply_matrices(self):
        self.matrix_A = self.input_matrix()
        self.matrix_B = self.input_matrix("second ")

        if len(self.matrix_A[1]) == len(self.matrix_B):
            for i in range(len(self.matrix_A)):
                self.result.append([])
                for k in range(len(self.matrix_B[0])):
                    sum = 0
                    for j in range(len(self.matrix_A[0])):
                        sum += self.matrix_A[i][j] * self.matrix_B[j][k]
                    self.result[i].append(sum)
            self.draw_a_board()
        else:
            print("The operation cannot be performed.")

    def main_diagonal(self):
        for i in range(len(self.matrix_A[0])):
            self.result.append([])
        for i in range(len(self.matrix_A[0])):
            for j in range(len(self.matrix_A[0])):
                self.result[j].append(self.matrix_A[i][j])

    def side_diagonal(self):
        self.vertical_line()
        vertical_transposed = self.result
        self.result = []
        for i in range(len(vertical_transposed[0])):
            self.result.append([])
        for i in range(len(vertical_transposed)):
            for j in range(len(vertical_transposed) - 1, -1, -1):
                self.result[i].append(vertical_transposed[j][i])

    def vertical_line(self):
        for i in range(len(self.matrix_A)):
            self.result.append([])
        for i in range(len(self.matrix_A)):
            for j in range(len(self.matrix_A[0]) - 1, -1, -1):
                self.result[i].append(self.matrix_A[i][j])

    def horizontal_line(self):
        for i in range(len(self.matrix_A) - 1, -1, -1):
            self.result.append(self.matrix_A[i])

    def create_submatrix(self, matrix, col, row=0):
        submatrix = []
        z = 0
        for x in range(len(matrix)):
            if x != row:
                submatrix.append([])
                for y in range(len(matrix[0])):
                    if y != col:
                        submatrix[z].append(matrix[x][y])
                z += 1
        return submatrix

    def calculate_determinant(self, matrix, operation="det"):
        det = 0
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0]
        elif len(matrix[0]) > 2:
            if operation == "det":
                for position in range(len(matrix[0])):
                    det += matrix[0][position] * (-1) ** (1 + (position + 1)) * self.calculate_determinant(self.create_submatrix(matrix, position))
                return det
            elif operation == "invers":
                for row in range(len(matrix)):
                    self.cofactors.append([])
                    for col in range(len(matrix[0])):
                        cof = (-1) ** (row + col + 2) * self.calculate_determinant(self.create_submatrix(matrix, col, row))
                        self.cofactors[row].append(cof)
        else:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    def inverse_matrix(self):
        matrix = self.input_matrix("")
        determinant = self.calculate_determinant(matrix)
        self.calculate_determinant(matrix, "invers")
        self.matrix_A = self.cofactors
        self.main_diagonal()
        transposed = self.result
        self.result = []
        try:
            self.multiply_by_constant(transposed, 1 / determinant)
        except ZeroDivisionError:
            print("This matrix doesn't have an inverse.")

    def menu(self):
        while True:
            print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices")
            print("4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
            user = input("Your choice: ")
            if user == "1":
                self.addindg()
            elif user == "2":
                matrix = self.input_matrix("")
                number = input("Enter constant: ")
                number = float(number) if "." in number else int(number)
                self.multiply_by_constant(matrix, number)
            elif user == "3":
                self.multiply_matrices()
            elif user == "0":
                break
            elif user == "4":
                print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
                user = input("Your choice: ")
                self.matrix_A = self.input_matrix("")
                if user == "1":
                    self.main_diagonal()
                elif user == "2":
                    self.side_diagonal()
                elif user == "3":
                    self.vertical_line()
                elif user == "4":
                    self.horizontal_line()
                self.draw_a_board()
                self.matrix_A = []
                self.result = []
            elif user == "5":
                matrix = self.input_matrix("")
                determinant = self.calculate_determinant(matrix)
                print("The result is:\n",determinant, sep="")
            elif user == "6":
                self.inverse_matrix()
            self.matrix_A = []
            self.matrix_B = []
            self.result = []
            print()

if __name__ == "__main__":
    operations_on_matrix = Matrixes()
    operations_on_matrix.menu()
