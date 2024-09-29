"""
Q5) What is the purpose continue statement in python?
Ans) The 'continue' statement in programming is used to skip the current iteration of a loop and proceed to the next iteration.

-> Purpose :
	1. Skip remaining code for a single iteration cycle.
	2. Improve Readability
	3. Efficiency

"""

for i in range(0, 6):
    if i == 2:
        continue
    print(i)


"""

O/P:
0
1
3
4
5

"""
