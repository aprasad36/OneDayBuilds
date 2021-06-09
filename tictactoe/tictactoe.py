class tictactoe():
    def __init__(self):
        self.player = 0
        self.board = [[-1 for i in range(3)] for j in range(3)]

    def place(self, x, y):
        try:
            if self.board[x][y] == -1:
                self.board[x][y] = self.player
                return True
            else:
                return False
        except:
            return False

    def printBoard(self):
        for i in self.board:
            for j in i:
                if j == -1:
                    print(".", end=" ")
                else:
                    print("x" if (j == 0) else "o", end=" ")
            print()

    def win(self, plr):
        # rows
        for i in self.board:
            count = 0
            for j in i:
                if (j != plr):
                    break
                count += 1
                if count == 3:
                    return True

        # cols
        for i in range(3):
            count = 0
            for j in range(3):
                if self.board[j][i] != plr:
                    break
                count += 1
                if count == 3:
                    return True

        # top-left to bot-right
        count = 0
        for i in range(3):
            if self.board[i][i] != plr:
                break
            count += 1
            if count == 3:
                return True

        # bot-left to top right
        count = 0
        for i in range(2, -1, -1):
            if self.board[2-i][i] != plr:
                break
            count += 1
            if count == 3:
                return True
        return False

    def draw(self):
        isDraw = True
        for i in self.board:
            for j in i:
                if j == -1:
                    isDraw = False
        return isDraw

    def read(self):
        while True:
            x = input("Enter an x y (0 to 2): ").split(" ")
            x = [int(i) for i in x]
            if self.place(x[0], x[1]):
                break
            else:
                print("Invalid input. Please try again.")

    def reset(self):
        self.board = [[-1 for i in range(3)] for j in range(3)]

    def main(self):
        while True:
            self.printBoard()
            self.read()
            if not self.win(self.player):
                if self.draw():
                    break
                self.player = 0 if self.player else 1
            else:
                break
        self.printBoard()
        if not self.draw():
            print(self.player, " wins!")
        else:
            print("Draw!")

running = True
while running:
    x = tictactoe()
    x.main()
    x.reset()
    tmp = input("Continue playing? [y, n]: ")
    running = (tmp == "y")
