import random
import os


class TicTacToe:
    def __init__(self):
        self.board: list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done: str = ""

    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def reset_board(self):
        self.board: list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done: str = ""

    def check_win_draw(self):
        dict_win = {}
        for i in ["X", "O"]:
            # Horizontal
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            # Vertical
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            # Diagonal
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "X"
            print("X Venceu!")
        elif dict_win["O"]:
            self.done = "O"
            print("O Venceu!")

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c += 1
                    break

        if c == 0:
            self.done = "D"
            print("Draw!")
            return

    def get_player_move(self):
        invalid_move = True
        while invalid_move:
            try:
                print("Digite a linha do seu movimento: ")
                x = int(input())

                print("Digite a coluna do seu movimento: ")
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Coordenadas inválidas")

                if self.board[x][y] != " ":
                    print("Posição já preenchida")
                    continue
            except Exception as e:
                print(e)
                continue
            invalid_move = False
        self.board[x][y] = "X"

    def make_move(self):
        list_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i, j))

        if len(list_moves) > 0:
            x, y = random.choice(list_moves)
            self.board[x][y] = "0"

tictactoe = TicTacToe()
tictactoe.print_board()
jogo = 0

while jogo == 0:
    os.system("cls")
    tictactoe.print_board()
    while tictactoe.done == "":
        tictactoe.get_player_move()
        tictactoe.make_move()
        os.system("cls")
        tictactoe.print_board()
        tictactoe.check_win_draw()

    print("Digite 1 para sair ou qualquer tecla para continuar")
    jogo = int(input())
    if next == 1:
        break
    else:
        tictactoe.reset_board()
        jogo = 0


