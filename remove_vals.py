import random
from puzzle_solve import puzzle_solve

def remove_vals(depth, difficulty, puzzle):
    """recursively remove values until puzzle reaches user-chosen difficulty"""
    if depth == difficulty:
        return puzzle
    
    complete = False
    # don't advance until puzzle is verified to still have a unique solution
    while complete == False:
        value = 0
        # find a random slot that is not already empty
        while value == 0:
            row = random.randint(0,8)
            column = random.randint(0,8)
            value = puzzle[row][column]

        # remove value from selected slot
        puzzle[row][column] = 0

        # if a unique solution does not exist, undo the last change
        if not puzzle_solve(puzzle):
            puzzle[row][column] = value
        else:
            complete = True

    # after completion, continue to next step
    remove_vals(depth + 1, difficulty, puzzle)
    
    return puzzle