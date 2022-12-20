result_path = []

def route_exists(from_row, from_column, to_row, to_column, map_matrix):          
    list_path = [(from_row, from_column)]    
    
    row_count = len(map_matrix)
    col_count = len(map_matrix[0])

    row_offsets = [-1, 0, 1, 0]
    col_offsets = [0, 1, 0, -1]  

    while list_path:
        current_row, current_column = list_path.pop()        
        map_matrix[current_row][current_column] = False

        result_path.append((current_row, current_column))
        dead_end = True

        if current_row == to_row and current_column == to_column:
            return True

        for row_offset, col_offset in zip(row_offsets, col_offsets):
            # compute the row and column indices of the neighboring cell
            neighbor_row = current_row + row_offset
            neighbor_col = current_column + col_offset

            # check if the neighboring cell is within the bounds of the map and is a road
            if (0 <= neighbor_row < row_count and 0 <= neighbor_col < col_count and map_matrix[neighbor_row][neighbor_col]):
                # add the neighboring cell to the queue
                dead_end = False
                list_path.append((neighbor_row, neighbor_col))
        
        if dead_end:
            result_path.pop()
                 
    return False
   

if __name__ == '__main__':
    # map_matrix = [
    #     [True, False, False],
    #     [True, True, False],
    #     [False, True, True]        
    # ];

    map_matrix = [
        [True, True, True],
        [True, True, False],
        [False, False, True]        
    ];

    print(route_exists(0, 1, 2, 2, map_matrix))
    print("Fanal path =", result_path)
    # print("End path =", list_path)