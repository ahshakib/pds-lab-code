import Pyro4

@Pyro4.expose
class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        board_str = "\n"
        for i in range(0, 9, 3):
            board_str += f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}\n"
            if i < 6:
                board_str += "---------\n"
        return board_str

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            if self.check_winner():
                return f"Player {self.current_player} wins!\n"
            elif " " not in self.board:
                return "It's a draw!\n"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                return self.display_board()
        else:
            return "Invalid move. Try again.\n"

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False


def main():
    daemon = Pyro4.Daemon()  # make a Pyro daemon
    ns = Pyro4.locateNS()  # find the name server
    uri = daemon.register(TicTacToe)  # register the greeting object as a Pyro object
    ns.register("example.tictactoe", uri)  # register the object with a name in the name server

    print("Tic Tac Toe Server is ready.")
    daemon.requestLoop()  # start the event loop of the server

if __name__ == "__main__":
    main()
