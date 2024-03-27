def mang_trung_hang(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i] == matrix[j]:
                return True
    return False
mang = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]
if mang_trung_hang(mang):
    print("Ma trận có ít nhất hai hàng giống nhau.")
else:
    print("Ma trận không có hai hàng nào giống nhau.")