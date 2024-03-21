def pascal(n):
    if n <= 0:
        print("Vui lòng nhập số nguyên dương n.")
        return

    triangle = [[0] * (n + 1) for _ in range(n + 1)]# Khởi tạo ma trận Pascal với kích thước n x n

    for i in range(n + 1):# Đặt giá trị ban đầu của hàng và cột đầu tiên là 1
        triangle[i][0] = 1
        triangle[i][i] = 1

    for i in range(2, n + 1):  #Tính các giá trị còn lại của tam giác Pascal
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    for i in range(n + 1):
        print("n=" + str(i), end=" ")
        for j in range(i + 1):
            print(triangle[i][j], end=" ")
        print()

# Ví dụ
n = int(input("nhap n: "))
pascal(n)
