#Writing out the code for a 50 x 100 game board would take a long time to do by hand. Use for loops to create a 50 x 100 two-dimensional array. You can decide whether you want to actually put something in for each element in the lists.

board = []
number = 0

for x in range(100):
    board.append([])
    for y in range(50):
        board[x].append(number)
        number += 1
