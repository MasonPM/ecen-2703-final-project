from z3 import *
import itertools
import sys


def puzzle_solve(puzzle):
    # 9x9 matrix of integer variables
    X = [[Int("x_%s_%s" % (i+1, j+1))
        for j in range(9)]
        for i in range(9)]

    # each square contains a value in {1, ..., 9}
    squares_rule = [And(1 <= X[i][j], X[i][j] <= 9)
        for i in range(9)
        for j in range(9)]

    # each row contains a digit at most once
    rows_rule = [Distinct(X[i])
        for i in range(9)]

    # each column contains a digit at most once
    cols_rule = [Distinct([ X[i][j]
        for i in range(9)])
        for j in range(9)]

    # each 3x3 cell contains a digit at most once
    cells_rule = [Distinct([X[3*i0 + i][3*j0 + j]
        for i in range(3)
        for j in range(3)])
        for i0 in range(3)
        for j0 in range(3)]

    # each square must receive a value
    solution_rule = [If(puzzle[i][j] == 0, True, X[i][j] == puzzle[i][j])
        for i in range(9) for j in range(9)]

    # combine all rules
    sudoku_c = squares_rule + rows_rule + cols_rule + cells_rule + solution_rule

    # check if solution exists
    s = Solver()
    s.add(sudoku_c)
    # check if solution exists
    if s.check() == sat:
        m = s.model()
        r = [[m.evaluate(X[i][j])
            for j in range(9)]
            for i in range(9)]
        print("+---+---+---+---+---+---+---+---+---+")
        for line in r:
            for square in line:
                if square == 0:
                    print("|   ", end = "")
                else:
                    print("| " + str(square) + " ", end = "")
            print("|\n+---+---+---+---+---+---+---+---+---+")
    else:
        print("failed to solve")


try:
    file = open("sudoku_output.txt","r")
except FileNotFoundError:
    print("sudoku_output.txt does not exist, run sudoku.py first!")
    sys.exit(1)

puzzle = []

for lines in file:
    puzzle.append(file.readline())

puzzle[:] = [line.split("|") for line in puzzle]

for i in range(len(puzzle)):
    while("" in puzzle[i]): 
        puzzle[i].remove("")
    while("\n" in puzzle[i]): 
        puzzle[i].remove("\n")
    for j in range(len(puzzle[i])):
        puzzle[i][j] = puzzle[i][j].replace("   ", "0")
        puzzle[i][j] = int(puzzle[i][j].replace(" ", ""))

puzzle = [line for line in puzzle if line != []]

puzzle_solve(puzzle)