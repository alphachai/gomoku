class Controller(object):
    def __init__():
        pass

    def make_move(self, board):
        pass


def RemoteController(Controller):
    def __init__():
        pass

    def make_move(self, board):
        pass


class Game(object):
    def __init__(local_first=True):
        self.players = [Controller()]
        self.players.insert(1 if local_first else 0, RemoteController())
        self.board = Board()

    def play(self):
        player = 0
        while(not self.game_over):
            board.add_move(self.players[player].make_move(board))
            player = 1 if player is 0 else 0

        #print results

    @property
    def game_over(self):
        return self.is_win(board.latest_move) or self.is_stalemate

    def is_win(self, latest_move=None):
        #if the latest move triggered a win
            #if latest_move is set, don't check the entire board
            #set results
            #return True
        #else
            #return False

    @property
    def is_stalemate(self):
        #if it's a stalemate
            #set results
            #return True
        #else
            #return False


class Board(object):
    history = []
    board = [[None for col in range(15)] for row in range(15)]

    def __init__():
        pass

    def add_move(self, move):
        if board[move.x][move.y] is not None:
            raise Exception("Tried to play checkers but senpai said no. (square taken)")
        else:
            board[move.x][move.y] = move.player
            history.append(move)

    @property
    def latest_move(self):
        return self.history[-1]

    def __repr__(self):
        out = ""
        for row in self.board:
            for square in row:
                out += " " if square is None else str(square)
            out += "\n"


class Move(object):
    def __init__(x, y, player)
        if x > 14 or y > 14:
            raise Exception("That move is out of bounds. (15x15)")
        self.x = x
        self.y = y
        self.player = player

    def __repr__(self):
        return 'Player {} played {},{}'.format(self.player, self.x, self.y)



