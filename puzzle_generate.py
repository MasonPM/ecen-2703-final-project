from random import sample

def puzzle_generate():
    """returns randomly generated, solved sudoku puzzle"""
    # define rows, columns, and numbers using sample to avoid duplicates in rows, columns, or cells
    rows = [g*3 + r
        for g in sample(range(3),3)
        for r in sample(range(3),3)] 
    
    cols = [g*3 + c
        for g in sample(range(3),3)
        for c in sample(range(3),3)]
    
    nums = sample(range(1,10),len(range(1,10)))

    # produce puzzle using initial random pattern
    puzzle = [[nums[(3*(r%3) + r//3 + c)%9]
        for c in cols]
        for r in rows]

    return puzzle
