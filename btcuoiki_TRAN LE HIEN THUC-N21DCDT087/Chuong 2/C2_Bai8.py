def TamGiacDuoi(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            if matrix[i][j] != 0:
                return False
    return True
matrix = [
    [1, 21, 0],
    [5, 3, 0],
    [4, 5, 6]
]
if TamGiacDuoi(matrix):
    print("Ma trận trên là ma trận tam giác dưới")
else:
    print("Ma trận trên không phải là ma trận tam giác dưới ")