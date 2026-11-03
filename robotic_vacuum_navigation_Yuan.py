## TASK 1

def distance_to_wall(world):

    no_rows = len(world)
    no_cols = len(world[0])
    for i in range(no_rows):
        for j in range(no_cols):
            if world[i][j] == 'X':
                row_start=i
                col_start=j
    # finding where the initial starting point of the vacuum cleaner is

    min_dist = None  # no wall found yet
    for i in range(no_rows):
        for j in range(no_cols):
            if world[i][j] == 'W':
                row_wall=i
                col_wall=j
                # finding where the wall is
                distance_to_wall = abs(row_start - row_wall) + \
                    abs(col_start - col_wall)
                # finding the distance from the wall to the vacuum cleaner
                if(min_dist is None):
                    min_dist = distance_to_wall
                elif(distance_to_wall < min_dist):
                    min_dist = distance_to_wall
                # comparing distance

    return min_dist


# TASK 2
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"

def make_move(world, direction):
    directions = [DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT]

    if(world is None or direction not in directions):
        return world

    no_rows = len(world)
    if no_rows == 0 or len(world[0]) == 0:
        return world
    no_cols = len(world[0])

    for i in range(no_rows):
        for j in range(no_cols):
            if world[i][j] == 'X':
                row_initial=i
                column_initial=j
                break
    # finding where the initial starting point of the vacuum cleaner is
    if direction == 'l':
        row_end= row_initial
        column_end = column_initial - 1

    if direction == 'r':
        row_end= row_initial
        column_end = column_initial + 1

    if direction == 'u':
        row_end = row_initial - 1
        column_end = column_initial

    if direction == 'd':
        row_end = row_initial + 1
        column_end = column_initial

    if row_end >= 0 and row_end < len(world):
        if column_end >= 0 and column_end < len(world[0]):
            if world[row_end][column_end] != 'W':
                world[row_end][column_end] = 'X'
                world[row_initial][column_initial] = 'E'

    # changing the respective elements in the world to 'X' and 'E'
    return world


## TASK 3
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"

def path_to_next(world):
    empty_list = []
    no_rows = len(world)
    no_cols = len(world[0])
    for i in range(no_rows):
        for j in range(no_cols):
            if world[i][j] == 'X':
                row_initial = i
                column_initial = j
                break
    # finding where the initial starting point of the vacuum cleaner is

    # Each candidate stores (distance, tie-break priority, movement list).
    # Priority: up (0), right (1), down (2), left (3).
    candidates = []

    for j, element in enumerate(world[row_initial]):
        if element == 'D' and j < column_initial:
            if 'W' not in world[row_initial][j + 1:column_initial]:
                distance = column_initial - j
                candidates.append((distance, 3, ['l'] * distance))
        elif element == 'D' and j > column_initial:
            if 'W' not in world[row_initial][column_initial + 1:j]:
                distance = j - column_initial
                candidates.append((distance, 1, ['r'] * distance))

    # finding the dirt to the left and right without looking through walls

    for i, element2 in enumerate(world):
        if element2[column_initial] == 'D' and i < row_initial:
            if all(world[k][column_initial] != 'W' for k in range(i + 1, row_initial)):
                distance = row_initial - i
                candidates.append((distance, 0, ['u'] * distance))
        elif element2[column_initial] == 'D' and i > row_initial:
            if all(world[k][column_initial] != 'W' for k in range(row_initial + 1, i)):
                distance = i - row_initial
                candidates.append((distance, 2, ['d'] * distance))
    # finding the dirt in the up and down directions without looking through walls

    if candidates:
        candidates.sort(key=lambda candidate: (candidate[0], candidate[1]))
        empty_list = candidates[0][2]

    return empty_list
