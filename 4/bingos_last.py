# 1. pre-process data
#   1.a. get sum for rows and columns in the beginning
#   1.b. store numbers' position.
#   1.c. set up initial sum counters for simulation
# 2. for each number, find the position
# 3. accumulate the row and column simulation sum
# 4. if the simulation sum is winning, calcluate the final score.
# 5. otherwise, go back to 2

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Deque, Optional
from collections import deque

def gen_board_slice():
    return [0, 0, 0, 0, 0]

@dataclass
class Board:
    sum_row: List[int] = field(default_factory=gen_board_slice)
    sum_column: List[int] = field(default_factory=gen_board_slice)
    num_position: Dict[int, Tuple] = field(default_factory=dict)
    marked_row: List[int] = field(default_factory=gen_board_slice)
    marked_column: List[int] = field(default_factory=gen_board_slice)
    acc_row: List[int] = field(default_factory=gen_board_slice)
    acc_column: List[int] = field(default_factory=gen_board_slice)

@dataclass
class Simulation:
    sequences: List[int]
    boards: Deque[Board]

def read_boards(input_filepath):
    boards = deque()

    with open(input_filepath) as infile:
        sequences = list(map(int, next(infile).strip().split(",")))

        idx_row = 0
        for line in infile:
            line = line.strip()
            if line == "":
                idx_row = 0
                boards.append(Board())
                continue

            idx_column = 0
            for num in map(int, line.split()):
                boards[-1].sum_row[idx_row] += num
                boards[-1].sum_column[idx_column] += num
                boards[-1].num_position[num] = (idx_row, idx_column)
                idx_column += 1

            idx_row += 1
    
    return Simulation(sequences, boards)

def run_simulation(simulation: Simulation):
    last_board = None
    last_seq = None

    for seq in simulation.sequences:
        for _ in range(len(simulation.boards)):
            board = simulation.boards.popleft()
            if seq in board.num_position:
                # print(seq)
                pos_row, pos_column = board.num_position[seq]
                board.acc_row[pos_row] += seq
                board.acc_column[pos_column] += seq
                board.marked_row[pos_row] += 1
                board.marked_column[pos_column] += 1

                if (board.marked_row[pos_row] == 5 or board.marked_column[pos_column] == 5) and (
                    board.acc_row[pos_row] == board.sum_row[pos_row] or (
                        board.acc_column[pos_column] == board.sum_column[pos_column])):
                    last_seq = seq
                    last_board = board
                    continue

            if len(simulation.boards) == 0:
                last_seq = seq
                last_board = board
            # print(last_board)
            simulation.boards.append(board)

    get_final_score(last_seq, last_board)

def get_final_score(last_number: Optional[int], board: Optional[Board]):
    if board is None or last_number is None:
        print("Nothing")
        return
    unmarked_sum = 0
    for idx, sum_row in enumerate(board.sum_row):
        unmarked_sum += sum_row - board.acc_row[idx]

    print(unmarked_sum, last_number)
    print(unmarked_sum*last_number)

if __name__ == "__main__":
    simulation = read_boards("input")
    # print(len(simulation.sequences), len(set(simulation.sequences)), len(simulation.boards))
    run_simulation(simulation)
