import sys
from puzzle_generate import puzzle_generate
from remove_vals import remove_vals

# check for correct command line argument usage
if len(sys.argv) != 2:
    print("usage: python sudoku.py [difficulty]")
    print("example: python sudoku.py 30")
    print("please select a difficulty between 10 and 55")
    sys.exit(1)

try:
    difficulty = int(sys.argv[1])
except ValueError:
    print("usage: python sudoku.py [difficulty]")
    print("example: python sudoku.py 30")
    print("please select a difficulty between 10 and 55")
    sys.exit(1)

if 10 > difficulty or difficulty > 55:
    print("usage: python sudoku.py [difficulty]")
    print("example: python sudoku.py 30")
    print("please select a difficulty between 10 and 55")
    sys.exit(1)

# recursively remove values from puzzle until requested difficulty is reached
puzzle = remove_vals(0, difficulty, puzzle_generate())

# return result to console and file
file = open("sudoku_output.txt","w+") 

print("+---+---+---+---+---+---+---+---+---+")
file.write("+---+---+---+---+---+---+---+---+---+\n")
for line in puzzle:
    for square in line:
        if square == 0:
            print("|   ", end = "")
            file.write("|   ")
        else:
            print("| " + str(square) + " ", end = "")
            file.write("| " + str(square) + " ")
    print("|\n+---+---+---+---+---+---+---+---+---+")
    file.write("|\n+---+---+---+---+---+---+---+---+---+\n")

print("puzzle written to sudoku_output.txt")
