def is_winner(board):
    for i in range(5):
        if board[i] == 'x' and board[i + 5] == 'x' and board[i + 10] == 'x' and board[i + 15] == 'x' and board[i + 20] == 'x':
            return True
        if board[5*i] == 'x' and board[5*i + 1] == 'x' and board[5*i + 2] == 'x' and board[5*i + 3] == 'x' and board[5*i + 4] == 'x':
            return True
    return False

def p1():
    with open('squid.txt') as f:
        lines = f.readlines()
        nums = []
        nums = lines[0].strip().split(',')
        boards = []
        for i in range(1, len(lines)):
            line = lines[i]
            if(line.strip() == ''):
                boards.append([])
            else:
                row_nums = line.strip().split(' ')
                row_nums = [val.strip() for val in row_nums if val != '']
                boards[len(boards) - 1].extend(row_nums)
        winning_board = None
        index = 0
        while not winning_board:
            num = str(nums[index])
            for board in boards:
                for i in range(len(board)):
                    if board[i] == num:
                        board[i] = 'x'
                if(is_winner(board)):
                    winning_board = board
                    break
            index += 1
        print(winning_board, flush=True)
        print(sum([int(x) for x in winning_board if x.isnumeric()])*int(num), flush=True)

def p2():
    with open('squid.txt') as f:
        lines = f.readlines()
        nums = []
        nums = lines[0].strip().split(',')
        boards = []
        for i in range(1, len(lines)):
            line = lines[i]
            if(line.strip() == ''):
                boards.append([])
            else:
                row_nums = line.strip().split(' ')
                row_nums = [val.strip() for val in row_nums if val != '']
                boards[len(boards) - 1].extend(row_nums)
        index = 0
        while len(boards) > 1:
            num = str(nums[index])
            board_index = 0
            while board_index < len(boards):
                board = boards[board_index]
                for j in range(len(board)):
                    if board[j] == num:
                        board[j] = 'x'
                if(is_winner(board)):
                    del boards[board_index]
                else:
                    board_index += 1
            index += 1
        while not is_winner(boards[0]):
            num = str(nums[index])
            for j in range(len(board)):
                if board[j] == num:
                    board[j] = 'x'
            if is_winner(board):
                break
            else:
                index += 1
        print(sum([int(x) for x in boards[0] if x.isnumeric()])*int(num), flush=True)

if __name__ == "__main__":
    p2()