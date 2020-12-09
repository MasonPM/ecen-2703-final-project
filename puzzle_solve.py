from z3 import *
import itertools


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
        # verify uniqueness of solution by attempting to find another
        model = s.model()
        block = []
        for z3_decl in model:
            arg_domains = []
            for i in range(z3_decl.arity()):
                domain, arg_domain = z3_decl.domain(i), []
                for j in range(domain.num_constructors()):
                    arg_domain.append(domain.constructor(j)())
                arg_domains.append(arg_domain)
            for args in itertools.product(*arg_domains):
                block.append(z3_decl(*args) != model.eval(z3_decl(*args)))
        s.add(Or(block))

        # if discovered solution is not unique, return false
        if s.check() == sat:
                return False
        # if discovered solution is unique, return true
        else:
                return True
    # if no solution was found, return false
    else:
        return False
