def spiral_matrix(size):
    if not size:
        return []
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    num = 1
    top, bottom, left, right = 0, size - 1, 0, size - 1

    while left <= right and top <= bottom:
        for c in range(left, right + 1):
            matrix[top][c] = num
            num += 1
        top += 1

        for r in range(top, bottom + 1):
            matrix[r][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1

    return matrix
            