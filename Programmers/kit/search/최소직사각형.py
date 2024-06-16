def solution(sizes):
    row = 0
    col = 0
    for x, y in sizes:
        if x < y :
            x, y = y, x
        row = max(row, x)
        col = max(col, y)
    return row * col