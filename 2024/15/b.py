def b(filename_bot: str, filename_moves: str):
    ROBOT = '@'
    BOX_LEFT = '['
    BOX_RIGHT = ']'
    WALL = '#'
    EMPTY = '.'

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

    substitute_lookup = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.'
    }
    with open(filename_bot) as file:
        graph = file.read()
        for key, val in substitute_lookup.items():
            graph = graph.replace(key, val)
        graph = graph.split('\n')

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

    def move_horizontal(rownum: int, colnum: int, instruction: str):
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
        while graph[non_box_row][non_box_col] in (BOX_LEFT, BOX_RIGHT):
            non_box_row += d_row
            non_box_col += d_col
        if graph[non_box_row][non_box_col] == EMPTY:
            if d_col > 0:
                for col_swap in range(non_box_col, next_col, -1):
                    graph[rownum][col_swap] = graph[rownum][col_swap - 1]
            else:
                for col_swap in range(non_box_col, next_col):
                    graph[rownum][col_swap] = graph[rownum][col_swap + 1]
            graph[rownum][next_col] = ROBOT
            graph[rownum][colnum] = EMPTY
            return next_row, next_col
        return rownum, colnum

    def move_vertical(rownum: int, colnum: int, instruction: str):
        d_row, d_col = move_lookup[instruction]
        next_row, next_col = rownum + d_row, colnum + d_col
        next_tile = graph[next_row][next_col]
        if next_tile == WALL:
            return rownum, colnum
        if next_tile == EMPTY:
            graph[next_row][next_col] = ROBOT
            graph[rownum][colnum] = EMPTY
            return next_row, next_col
        if next_tile == BOX_LEFT:
            if can_move_box(next_row, colnum, d_row):
                move_box(next_row, next_col, d_row)
                graph[next_row][next_col] = ROBOT
                graph[rownum][colnum] = EMPTY
                return next_row, next_col
            return rownum, colnum
        else:
            if can_move_box(next_row, colnum - 1, d_row):
                move_box(next_row, colnum - 1, d_row)
                graph[next_row][next_col] = ROBOT
                graph[rownum][colnum] = EMPTY
                return next_row, next_col
            return rownum, colnum
    
    def can_move_box(rownum: int, colnum: int, d_row: int):
        next_row = rownum + d_row
        L = graph[next_row][colnum]
        R = graph[next_row][colnum + 1]
        if L == WALL or R == WALL:
            return False
        if L == R == EMPTY:
            return True
        if L == BOX_LEFT:
            return can_move_box(next_row, colnum, d_row)
        if L == BOX_RIGHT:
            if not can_move_box(next_row, colnum - 1, d_row):
                return False
        if R == BOX_LEFT:
            if not can_move_box(next_row, colnum + 1, d_row):
                return False
        return True

    def move_box(rownum: int, colnum: int, d_row: int):
        next_row = rownum + d_row
        L = graph[next_row][colnum]
        R = graph[next_row][colnum + 1]
        if L == WALL or R == WALL:
            return
        if L == R == EMPTY:
            graph[next_row][colnum] = BOX_LEFT
            graph[next_row][colnum + 1] = BOX_RIGHT
            graph[rownum][colnum] = graph[rownum][colnum + 1] = EMPTY
            return
        if L == BOX_LEFT:
            move_box(next_row, colnum, d_row)
            graph[next_row][colnum] = BOX_LEFT
            graph[next_row][colnum + 1] = BOX_RIGHT
            graph[rownum][colnum] = graph[rownum][colnum + 1] = EMPTY
            return
        if L == BOX_RIGHT:
            move_box(next_row, colnum - 1, d_row)
        if R == BOX_LEFT:
            move_box(next_row, colnum + 1, d_row)
        graph[next_row][colnum] = BOX_LEFT
        graph[next_row][colnum + 1] = BOX_RIGHT
        graph[rownum][colnum] = graph[rownum][colnum + 1] = EMPTY


    for id, instruction in enumerate(moves):
        if instruction in (LEFT, RIGHT):
            robot_row, robot_col = move_horizontal(robot_row, robot_col, instruction)
        else:
            robot_row, robot_col = move_vertical(robot_row, robot_col, instruction)
    
    res = 0
    for rownum, row in enumerate(graph):
        for colnum, tile in enumerate(row):
            if tile == BOX_LEFT:
                score = rownum * 100 + colnum
                # print(f"({rownum}, {colnum}): {score}")
                res += score
    return res



# print(b('example_bot_small.txt', 'example_moves_small.txt'))
print(b('example_bot_large.txt', 'example_moves_large.txt'))
print(b('input_bot.txt', 'input_moves.txt'))