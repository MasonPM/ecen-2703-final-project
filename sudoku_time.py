import sys
import timeit
from puzzle_generate import puzzle_generate
from remove_vals import remove_vals

file = open("timer_output.csv","w+")

for i in range(56):
    starttime = timeit.default_timer()
    remove_vals(0, i, puzzle_generate())
    endtime = timeit.default_timer()
    print(endtime - starttime)
    file.write(str(i) + "," + str(endtime - starttime) + "\n")