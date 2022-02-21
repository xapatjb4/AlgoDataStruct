# def knightsTour(n):
#   board = [[-1]*n for _ in range(n)]
#   board[0][0] = 0
#   if sh(board, 1, 0, 0):
#     print(board)

# def sh(board, moveNum, x,y):
#   if moveNum == len(board) * len(board: #minsing paran
#     return True
#   moves = getMoves(board, x,y)
#   for move in moves:
#     board[move[0]][move[1]] = moveNum
#     if sh(board, moveNum + 1, move[0], move[1]):
#       return True
#     board[move[0]][move[1]] = -1
#   return False

# def getMoves(board, x,y):
#   pm = set()
#   for move in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2), (-1,2),(1,-2), (-1,-2)]:
#     if move[0] + x < len(board) and move[0] + x > -1:
#       if move[1] + y < len(board) and move[1] + y > -1:
#         #bug, did not check whether spot was already visited
#         pm.add((move[0],move[1]) #bug missing parant
#   return pm
def knightsTour(n):
    board = [[-1]*n for _ in range(n)]
    board[0][0] = 0
    if sh(board, 1, 0, 0):
        for row in board:
            print(row)


def sh(board, moveNum, x, y):
    if moveNum == len(board) * len(board):
        return True
    moves = getMoves(board, x, y)
    for move in moves:
        board[move[0]][move[1]] = moveNum
        if sh(board, moveNum + 1, move[0], move[1]):
            return True
        board[move[0]][move[1]] = -1
    return False


def getMoves(board, x, y):
    pm = set()
    for move in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
        if move[0] + x < len(board) and move[0] + x > -1:
            if move[1] + y < len(board) and move[1] + y > -1:
                if board[move[0]+x][move[1]+y] == -1:
                    pm.add((move[0] + x, move[1]+y))
    return pm


knightsTour(8)
