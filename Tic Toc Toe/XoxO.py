from os import system
class TicTocToe:
    def __init__(self):
        self.board = [["   "] * 3, ["   "] * 3, ["   "] * 3]
        self.playerid = {1: "X", -1: "O"}
        self.playing =True
        self.position=None
        self.position_list = [['1','1'],['1','2'],['1','3'],
                             ['2','1'],['2','2'],['2','3'],
                             ['3','1'],['3','2'],['3','3']]
        self.player=None
        self.have_winner=False
        self.winner = None
        self.is_draw = False
    def choose_first_move(self):
        choose = input("Enter the first player (X/O): ").upper()
        while (choose != "X" and choose != 'O'):
            choose = input(f"{choose} is invalid, enter the first player: ").upper()
        print(f"{choose} goes first")
        self.player = 1 if choose == "X" else -1
    def move(self):
        print(f"{self.playerid[self.player]} turn!")
        self.position = input("Enter the position (row col): ").split()
        while self.position not in self.position_list or self.board[int(self.position[0])-1][int(self.position[1])-1]!="   ":
                print("Invalid position!")
                self.position = input("Enter the position (row col): ").split()
        self.position = list(map(int,self.position))
    def print_match(self):
        system("cls")
        self.board[self.position[0]-1][self.position[1]-1] = f" {self.playerid[self.player]} "
        for row in range(3):
            for i in range(13):
                print("-", end="")
            print("")
            for i in range(3):
                print("|", end=f"{self.board[row][i]}")
            print("|")
        for i in range(13):
            print("-", end="")
        print("")
    def is_having_winner(self):
        for i in range(3):
            if self.board[0][i]!="   " and self.board[0][i] == self.board[1][i] and self.board[1][i]==self.board[2][i]:
                self.have_winner=True
                self.winner=self.board[0][i][1]
                break
            if self.board[i][0]!="   " and self.board[i][0] == self.board[i][1] and self.board[i][2]==self.board[i][1]:
                self.have_winner=True
                self.winner=self.board[i][0][1]
                break
        if self.board[0][0]!="   " and self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
            self.have_winner=True
            self.winner==self.board[1][1][1]
        if self.board[0][2]!="   " and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            self.have_winner = True
            self.winner = self.board[1][1][1]
        if (self.have_winner):
            print(f"{self.winner} WIN!" )
            self.playing = False
    def draw(self):
        self.is_draw=True
        for i in self.board:
            for j in i:
                if j=="   ":
                    self.is_draw=False
        if self.is_draw and not self.have_winner:
            print("DRAW")
            self.playing=False
    def play(self):
        self.choose_first_move()
        while self.playing:
            self.move()
            self.print_match()
            self.player=-self.player
            self.is_having_winner()
            self.draw()
        choose = input("Enter Y to play again, else to exit: ")
        while(choose.lower()=="y"):
            self.play()
game=TicTocToe()
game.play()