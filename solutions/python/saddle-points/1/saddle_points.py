def saddle_points(matrix):
    if not matrix: 
        return []
    row_length = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != row_length:
            raise ValueError('irregular matrix')
    maxes_in_rows = [max(row) for row in matrix]
    mins_in_columns = [min(row[i] for row in matrix) for i in range(row_length)]
    trees = []
    for row_num, row in enumerate(matrix):
        for col_num, value in enumerate(row):
            if mins_in_columns[col_num] == value == maxes_in_rows[row_num]:
                trees.append({'row': row_num + 1, 'column': col_num + 1})
    return trees