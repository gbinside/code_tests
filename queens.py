"""
The usual problem on N queens on a NxN board, placed without menacing each other.
Normally solved with BackTracing.
"""

SIZE = 8

def calc_moves(board, row):
    moves = list(range(SIZE))  # I can do all this moves 0..N-1, then I remove some of them
    if row in board:
        moves = [x for x in moves if x>board[row]]  # if I am recomputing a line I already have, I consider higher Queen position than the last tried.
    for k,v in board.items():  # for all the queens already on the board
        if k>=row:  # if I am on the same row or a bigger one, skip, I am backtracing
            continue
        try:
            moves.remove(v)  # remove vertical queen attacked cells
        except:
            pass
        try:
            moves.remove(v-(row-k))  # remove diagonal going down-left
        except:
            pass
        try:
            moves.remove(v+(row-k))  # remove diagonal going down-right
        except:
            pass
    return moves

def n(board=None): 
    """
    compute the next board, given a board as a dict of queens positions [row]->column
    """
    if board is None:
        board = dict()  # the board is an dict [row(0..N-1)] => queen_position(0..N-1)
    row = len(board)  # row to compute
    moves = None
    while not moves:  # while there are no moves...
        moves = calc_moves(board, row)  # compute the moves.
        if moves:  # if there are move, take the first one
            board[row] = moves[0]
        else:  # if there are now moves
            if row in board:  # remove current line form the board if present
                del board[row] 
            row -= 1  # go back 1 row, I keep the board[row] (now board[row-1]) because I need it at line 11 to computer the backtracing. Basically here I am remembeing were to fork and go on.
    return board

if __name__ == "__main__":
    b = {}  # we can start with some board constraint, like b = {0:0} to start with a queen in top-left position.
    while len(b)<SIZE:
        b = n(b)  # froma board state I get the next board state
        print(b)  # print the board at every loop
