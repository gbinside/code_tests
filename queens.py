SIZE = 8

def calc_moves(board, row):
    moves = list(range(SIZE))
    if row in board:
        moves = [x for x in moves if x>board[row]]
    for k,v in board.items():
        if k>=row:
            continue
        try:
            moves.remove(v)
        except:
            pass
        try:
            moves.remove(v-(row-k))
        except:
            pass
        try:
            moves.remove(v+(row-k))
        except:
            pass
    return moves

def n(board=None):
    if board is None:
        board = dict()
    row = len(board)
    moves = None
    while not moves:
        moves = calc_moves(board, row)
        if moves:
            board[row] = moves[0]
        else:
            if row in board:
                del board[row]
            row -= 1
    return board

b = {}
while len(b)<SIZE:
    b = n(b)
    print(b)
