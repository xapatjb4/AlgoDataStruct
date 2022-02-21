
def solve_sudoku_puzzle(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    solve(board, 0)
    print('wtf')
    return board


def solve(board, pos):
    if pos == 81:
        return True
    x, y = getxy(pos)
    if board[x][y] != 0:
        return solve(board, pos+1)
    posm = getpm(board, x, y)
    for pm in posm:
        board[x][y] = pm
        if solve(board, pos+1):
            return True
        board[x][y] = 0
    return False


def getxy(n):
    return n//9, n % 9


def getpm(board, x, y):
    pm = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print('wtf!')
    for num in board[x]:
        if num in pm:
            pm.remove(num)
    for i in range(9):
        num = board[i][y]
        if num in pm:
            pm.remove(num)

    for i in range((x//3)*3, 3*(x//3 + 1)):
        for j in range((y//3)*3, 3 * (y//3 + 1)):
            if board[i][j] in pm:
                pm.remove(board[i][j])
    return pm


solve_sudoku_puzzle(
    [
        [8, 4, 9, 0, 0, 3, 5, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 9, 0, 0, 8, 3],
        [0, 0, 0, 9, 4, 6, 7, 0, 0],
        [0, 8, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 6, 8, 7, 2, 0, 0, 0],
        [5, 7, 0, 0, 1, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 1, 7, 0, 0, 8, 6, 5]
    ]
)
