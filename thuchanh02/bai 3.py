def count_letters(word):
    letter_count = {}  # Tạo một từ điển để lưu trữ số lần xuất hiện của mỗi chữ cái

    # Duyệt qua từng ký tự trong từ
    for char in word:
        # Tăng giá trị của key char (nếu tồn tại) hoặc tạo mới key char với giá trị là 1
        letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count
# Kiểm tra với một từ đã cung cấp
word = "hello"
print(count_letters(word))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
