class TicTacToe():

    def __init__(self):
        # system zero jedynkowy
        self.state = None
        self.matrix = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def winner(self, matrix):  # vertical and horizontal winner
        for row in matrix:
            if " " not in row:
                if all(row) == True:
                    self.state = "X wins"
                    break
                elif any(row) == False:
                    self.state = "O wins"

    def inverse_matrix(self, matrix):  # inversing matrix for horizontal checking
        matrix2 = [[], [], []]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix2[col].append(matrix[row][col])
        self.winner(matrix2)

    def diagonal_winner(self):
        diagonal1 = [self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]]
        diagonal2 = [self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]]
        if " " not in diagonal1 and " " not in diagonal2:
            if all(diagonal1) == True or all(diagonal2) == True:
                self.state = "X wins"
            elif any(diagonal1) == False or any(diagonal2) == False:
                self.state = "O wins"

    def draw(self):
        for row in self.matrix:
            if " " in row:
                break
        else:
            self.state = "Draw"

    def display_board(self):
        print(9 * "-")
        for x in range(3):
            print("| ", end="")
            for y in range(3):
                if self.matrix[x][y] == 1:
                    print("X", end = " ")
                elif self.matrix[x][y] == 0:
                    print("O", end=" ")
                else:
                    print(self.matrix[x][y], end=" ")
            print("|")
        print(9 * "-")

    def errors(self, coordinates):
        if  0 <= coordinates[0] < 3 and 0 <= coordinates[1] < 3:
            if self.matrix[coordinates[0]][coordinates[1]] == " ":
                return coordinates
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")

    def user_coordinates(self,  sign):
        while True:
            try:
                coordinates = [int(x) - 1 for x in input("Enter the coordinates: ").split(" ")]
            except ValueError:
                print("You should enter numbers!")
            else:
                coordinates = self.errors(coordinates)
                if type(coordinates) == list:
                    self.matrix[coordinates[0]][coordinates[1]] = sign
                    break

    def checking_state_of_game(self):
        matrix2 = self.matrix
        self.winner(matrix2)
        if self.state is None:
            self.inverse_matrix(matrix2)
            if self.state is None:
                self.diagonal_winner()
                if self.state is None:
                    self.draw()

    def main(self):
        count = 1
        self.display_board()
        while True:

            if count % 2 == 0:
                sign = 0
            else:
                sign = 1
            self.user_coordinates(sign)
            self.checking_state_of_game()
            self.display_board()
            if self.state != None:
                print(self.state)
                break
            count += 1

tictactoe = TicTacToe()
tictactoe.main()

