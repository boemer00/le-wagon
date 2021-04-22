def sudoku_validator(grid):
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in grid:
        if sorted(row) != number:
            return False
    
    for column in zip(*grid):
        if sorted(column) != number:
            return False
    
    for i in range(3):
        for j in range(3):
            region = []
            for line in grid[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            if sorted(region) != number:
                return False
    return True
