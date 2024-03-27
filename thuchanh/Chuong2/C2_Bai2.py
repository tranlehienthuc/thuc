def mang_tam_giac_tren(matrix):
    for i in range(1, len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

mang = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]
if mang_tam_giac_tren(mang):
    print("Ma trận trên là ma trận tam giác")
else:
    print("Ma trận trên không phải là ma trận tam giác ")