# 4-1
with open("input4-1-lange.txt", "r") as f:
    data = f.read().split("\n")

boards = []
current_board = []
split_counter = 0

# Split up boards and numbers
for value in data:
    if value == "":
        split_counter += 1
        if len(current_board) > 0:
            boards.append(current_board)
            current_board = []
            continue
        continue
    if split_counter == 0:
        numbers = value
    else:
        current_board.append([[v, False] for v in value.split(" ") if len(v) > 0])
if len(current_board) > 0:
    boards.append([r for r in current_board if len(r) > 0])

def find_winner(numbers, boards, final=False):
    winners = []
    
    
    
    # Start processing numbers
    for n in numbers:
        # Check for matches and update
        for k, board in enumerate(boards):
            for j, row in enumerate(board):
                for i, value in enumerate(row):
                    if n == value[0]:
                        #print(f"Found {n} in board={k} row={j} and pos={i}")
                        row[i] = [n, True]
        
        # Check for winners
        for k, board in enumerate(boards):
            #print("Winners so far: ", winners)
            
            # Check if winner has x-axis win
            for j, row in enumerate(board):
                if sum([v[1] for v in row]) == 5:
                    print(f"Bingo!!! We have x-axis winner. Board={k} Row={j}. Winning number={n}")
                    # if not final board return board else continue until you find the final
                    if not final:
                        return board, n
                    else:
                        if k not in winners:
                            winners.append(k)
                        if len(boards) == len(winners):
                            return board, n
            

            # Check if winner has y-axis win
            for i in range(len(board)):
                if sum([v[1] for v in [row[i] for row in board]]) == 5:
                    print(f"Bingo!!! We have y-axis winner. Board={k} Rows pos={i}. Winning number={n}")
                    # if not final board return board else continue until you find the final
                    if not final:
                        return board, n
                    else:
                        if k not in winners:
                            winners.append(k)
                        if len(boards) == len(winners):
                            return board, n

import copy
final_boards = copy.deepcopy(boards)

winner, winning_num, *args = find_winner(numbers.split(","), boards)
winning_score = sum([int(element[0]) for sub in winner for element in sub if element[1] == False])
print("Result 1: ", winning_score * int(winning_num))

winner, winning_num = find_winner(numbers.split(","), final_boards, final=True)
winning_score = sum([int(element[0]) for sub in winner for element in sub if element[1] == False])
print("Result 2: ", winning_score * int(winning_num))
