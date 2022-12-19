def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    # left_move = [0, -1]
    # right_move = [0, 1]
    # top_move = [-1, 0]
    # bottom_move = [1, 0]
    
    row_offsets = [-1, 0, 1, 0]
    col_offsets = [0, 1, 0, -1]    

    list_path = [(from_row, from_column)]
    # map_matrix[from_row][from_column] = True
    
    row_count = len(map_matrix)
    col_count = len(map_matrix[0])

    # temp_route = [[False for _ in range(col_count)] for _ in range(row_count)]
    # temp_route[from_row][from_column] = True
    # print("temp_route =", temp_route)

    while list_path:
        print("Before pop list_path =", list_path)
        current_row, current_column = list_path.pop(0)        
        print(current_row, current_column)
        print("After pop list_path =", list_path)

        if current_row == to_row and current_column == to_column:            
            return True

        # end_neighbore = True

        for row_offset, col_offset in zip(row_offsets, col_offsets):
            # compute the row and column indices of the neighboring cell
            neighbor_row = current_row + row_offset
            neighbor_col = current_column + col_offset

            # check if the neighboring cell is within the bounds of the map and is a road
            if (0 <= neighbor_row < row_count and 0 <= neighbor_col < col_count and map_matrix[neighbor_row][neighbor_col]):
                # mark the neighboring cell as visited
                map_matrix[neighbor_row][neighbor_col] = False
                print("map_matrix =", map_matrix)
                # end_neighbore = False

                # add the neighboring cell to the queue
                list_path.append((neighbor_row, neighbor_col))
        
        # if all the neightboring cells were False and not equal target (to_row, to_column), Set current cell to False
        # if end_neighbore:
        #     map_matrix[current_row][current_column] = False      
        #     print(map_matrix)      
        
    return False

    # for i, row in enumerate(map_matrix):     
    #     row_offset = []                   
    #     if i == 0:
    #         # if row == 0, check only bottom position
    #         row_offset.append(1)
    #     elif i == len(map_matrix) - 1:
    #         # if row == last row, check only above position
    #         # print("Last row count =", len(map_matrix) - 1)
    #         row_offset.append(-1)
    #     else:
    #         # check above and bottom position, twice time
    #         row_offset = [1, -1]

    #     for j, col in enumerate(row):
    #         if j == 0:
    #             # if col == 0, check only right position
    #             pass                    
    #         elif j == len(map_matrix[0]) - 1:
    #             # if col == last column, check only left position
    #             print("Last culumn count =", len(map_matrix[0]) - 1)
    #         else:
    #             # Check left and right position, twice time
    #             pass
    #         # print("row:{0} | col:{1} | value:{2}".format(i,j,col))

    #         if i == to_row and j == to_column:
    #             return True
    # return False

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]        
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))