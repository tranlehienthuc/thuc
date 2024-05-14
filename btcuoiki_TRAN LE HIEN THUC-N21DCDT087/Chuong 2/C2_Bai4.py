def NhomHang(matrix):
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        print("Ma trận không phải là ma trận vuông.")
        return
    row_groups = {}

    for i in range(n):
        for j in range(i+1, n):
            if matrix[i] == matrix[j]:
                if i not in row_groups:
                    row_groups[i] = [i]
                row_groups[i].append(j)
    
    for group in row_groups.values():
        print("Nhóm hàng giống nhau:", group)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]
NhomHang(matrix)