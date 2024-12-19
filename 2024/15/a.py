def a(filename_bot: str, filename_moves: str):
    with open(filename_bot) as file:
        graph = file.read().split('\n')

    with open(filename_moves) as file:
        moves = file.read().replace('\n', '')

    graph = [list(row) for row in graph]
    robot_found = False
    for rownum, row in enumerate(graph):
        for colnum, tile in enumerate(row):
            if tile == ROBOT:
                robot_row, robot_col = rownum, colnum
                robot_found = True
                break
        if robot_found:
            break
   
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'
    move_lookup = {
        UP: (-1, 0), 
        DOWN: (1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1)
    }
    def move(rownum: int, colnum: int, instruction: str):
        d_row, d_col = move_lookup[instruction]
        next_row, next_col = rownum + d_row, colnum + d_col
        next_tile = graph[next_row][next_col]
        if next_tile == WALL:
            return rownum, colnum
        if next_tile == EMPTY:
            graph[next_row][next_col] = ROBOT
            graph[rownum][colnum] = EMPTY
            return next_row, next_col
        non_box_row, non_box_col = next_row, next_col
        while graph[non_box_row][non_box_col] == BOX:
            non_box_row += d_row
            non_box_col += d_col
        if graph[non_box_row][non_box_col] == EMPTY:
            graph[non_box_row][non_box_col] = BOX
            graph[next_row][next_col] = ROBOT
            graph[rownum][colnum] = EMPTY
            return next_row, next_col
        return rownum, colnum
        
    for instruction in moves:
        robot_row, robot_col = move(robot_row, robot_col, instruction)
    
    res = 0
    for rownum, row in enumerate(graph):
        for colnum, tile in enumerate(row):
            if tile == BOX:
                score = rownum * 100 + colnum
                # print(f"({rownum}, {colnum}): {score}")
                res += score
    return res

ROBOT = '@'
BOX = 'O'
WALL = '#'
EMPTY = '.'


print(a('example_bot_small.txt', 'example_moves_small.txt'))
print(a('example_bot_large.txt', 'example_moves_large.txt'))
print(a('input_bot.txt', 'input_moves.txt'))