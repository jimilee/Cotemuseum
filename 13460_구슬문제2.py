
def make_board(input):
    inputs = input.split('\n')
    print(inputs)
    board = []
    where_R, where_B, where_O = [],[],[]
    N = int(inputs[0].split(' ')[0])
    M = int(inputs[0].split(' ')[1])
    for n in range(N):
        board.append([])
        for m in range(M):
            board[n].append(inputs[n+1][m])
            #구슬, 구멍 좌표 저장
            if inputs[n+1][m] == 'R':
                where_R.append(n)
                where_R.append(m)
            elif inputs[n+1][m] == 'B':
                where_B.append(n)
                where_B.append(m)
            elif inputs[n+1][m] == 'O':
                where_O.append(n)
                where_O.append(m)
            # print(inputs[n+1].split(maxsplit=-1))

    init_state = board

    move_the_board(init_state, board, where_R, where_B, where_O)

def direction_check(board, where):
    print('moving balls')
    #공 방향 체크(상하좌우)
    d_list = {'up': False, 'down': False, 'left': False, 'right': False}
    if board[where[0] - 1][where[1]] == '.' or board[where[0] - 1][where[1]] == 'O':
        d_list['up'] = True
    elif board[where[0] + 1][where[1]] == '.' or board[where[0] + 1][where[1]] == 'O':
        d_list['down'] = True
    elif board[where[0]][where[1] - 1] == '.' or board[where[0]][where[1] - 1] == 'O':
        d_list['left'] = True
    elif board[where[0]][where[1] + 1] == '.' or board[where[0]][where[1] + 1] == 'O':
        d_list['right'] = True

    return d_list

def move_balls(board, where_R, where_B, tilt):
    tilt_ = {'up': [0,1], 'down': [0,-1], 'left': [-1,0], 'right': [1,0]}

def move_the_board(init_state, board, where_R, where_B, where_O):
    print(where_B, where_O, where_R)
    # B 구슬이 구멍에 빠지면 안되고, R이 구멍으로 가야댐
    dist_R = int(abs(where_R[0]-where_O[0]) + abs(where_R[1] - where_O[1]))
    dist_B = int(abs(where_B[0] - where_O[0]) + abs(where_B[1] - where_O[1]))
    print('구슬 B의 거리 : ',dist_B,'구슬 R의 거리 : ', dist_R)
    total_cnt = 0
    while dist_R != 0 or total_cnt > 10:
        Up, Down, Left, Right = False, False,False,False
        if board[where_R[0] - 1][where_R[1]] == '.':
            Up = True
        elif board[where_R[0] + 1][where_R[1]] == '.':
            Down = True
        elif board[where_R[0]][where_R[1] - 1] == '.':
            Left = True
        elif board[where_R[0]][where_R[1] + 1] == '.':
            Right = True
        if where_R[0] < where_O[0] and Right:
            cnt_right=+1





input = '5 5\n#####\n#..B#\n#.#.#\n#RO.#\n#####'
input = '3 7\n#######\n#R.O.B#\n#######\n'
make_board(input)