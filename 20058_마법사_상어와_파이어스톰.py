import copy


def tornado(start, end, board):
    tmp = copy.deepcopy(board)
    N = end - start
    for i in range(start, end):
        print(i)
        board[i][end] = tmp[start][i]
        board[end][end-i] = tmp[i][end]
        board[i][start] = tmp[end][i]
        board[start][i] = tmp[end-i][start]
    if N > 2:
        print('tornado', start+1, end-1, board)
        tornado(start+1, end-1, board)

    print(board)
board = [[1,2,3,4],[9,10,11,12],[17,18,19,20],[25,26,27,28]]
tornado(0,3,board)
