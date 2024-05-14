import os  # Nhập module os để tương tác với hệ thống tệp và thư mục

def add_word(dictionary):  # Hàm để thêm từ mới vào từ điển
    word = input("Nhập từ: ")  # Nhập từ
    meanings = []  # Khởi tạo danh sách để lưu các nghĩa của từ
    while True:  # Tạo vòng lặp để nhập nhiều nghĩa cho từ
        meaning = input("Nhập nghĩa: ")  # Nhập nghĩa của từ 
        if not meaning:  # Nếu không có nghĩa được nhập (rỗng) thì dừng vòng lặp
            break
        example = input("Nhập ví dụ: ")  # Nhập ví dụ cho nghĩa của từ
        meanings.append((meaning, example))  # Thêm cặp (nghĩa, ví dụ) vào danh sách nghĩa
    dictionary[word] = meanings  # Thêm từ và các nghĩa của nó vào từ điển

def remove_word(dictionary):  # Hàm để xóa từ khỏi từ điển
    word = input("Nhập từ cần xóa: ")  # Nhập từ cần xóa 
    if word in dictionary:  # Kiểm tra nếu từ tồn tại trong từ điển
        del dictionary[word]  # Xóa từ khỏi từ điển
        print(f"Từ '{word}' đã được xóa khỏi từ điển.")
    else:
        print(f"Từ '{word}' không tồn tại trong từ điển.")  # Thông báo nếu từ không có trong từ điển

def lookup_word(dictionary):  # Hàm để tra cứu nghĩa của từ
    word = input("Nhập từ cần tra cứu: ")  # Nhập từ cần tra cứu
    if word in dictionary:  # Kiểm tra nếu từ tồn tại trong từ điển
        meanings = dictionary[word]  # Lấy danh sách nghĩa của từ
        print(f"Những nghĩa của '{word}':")
        for i, (meaning, example) in enumerate(meanings, start=1):  # In các nghĩa và ví dụ
            print(f"{i}. {meaning}: {example}")
    else:
        print(f"Từ '{word}' không tồn tại trong từ điển.")  # Thông báo nếu từ không có trong từ điển

def save_dictionary(dictionary, filename):  # Hàm để lưu từ điển vào tệp
    with open(filename, 'w') as file:  
        for word, meanings in sorted(dictionary.items()):  # Duyệt từng từ và nghĩa trong từ điển và ghi vào tệp
            file.write(word + '\n')  # Ghi từ vào tệp
            for meaning, example in meanings:  # Duyệt các nghĩa của từ và ghi vào tệp
                file.write('\t' + meaning + '\n')  # Ghi nghĩa vào tệp
                file.write('\t\t' + example + '\n')  # Ghi ví dụ vào tệp
                
def load_dictionary(filename):  # Hàm để nạp từ điển từ tệp
    dictionary = {}  # Khởi tạo từ điển rỗng
    if os.path.exists(filename):  # Kiểm tra nếu tệp tồn tại
        with open(filename, 'r') as file:  # Mở tệp để đọc
            current_word = None  # Khởi tạo từ hiện tại
            for line in file:  # Duyệt từng dòng trong tệp
                line = line.strip()  # Loại bỏ khoảng trắng và ký tự xuống dòng từ dòng đọc
                if not line:  # Bỏ qua dòng trống
                    continue
                if not line.startswith('\t'):  # Nếu không bắt đầu bằng tab, đây là từ mới
                    current_word = line  # Lưu từ hiện tại
                    dictionary[current_word] = []  # Tạo danh sách nghĩa cho từ mới
                else:  # Nếu bắt đầu bằng tab, đây là nghĩa của từ
                    if line.startswith('\t\t'):  # Nếu là tab thứ 2, đây là ví dụ
                        dictionary[current_word][-1] = (dictionary[current_word][-1][0], line.strip())  # Cập nhật ví dụ
                    else:  # Nếu là tab đầu tiên, đây là nghĩa mới
                        dictionary[current_word].append((line.strip(), ''))  # Thêm nghĩa mới vào danh sách nghĩa
    return dictionary  # Trả về từ điển đã nạp từ tệp

def print_dictionary(dictionary):  # Hàm để in từ điển ra màn hình
    for word, meanings in sorted(dictionary.items()):  # Duyệt từng từ và nghĩa trong từ điển
        print(word)  # In từ ra màn hình
        for meaning, example in meanings:  # Duyệt các nghĩa và ví dụ của từ và in ra màn hình
            print(f"\t{meaning}: {example}")

def main():  # Hàm main để chạy chương trình
    student_id = "n21dcdt087" 
    filename = f"{student_id}_mang.txt"  # Tên tệp từ điển
    dictionary = load_dictionary(filename)  # Thêm từ điển vào tệp

    while True:  # Bắt đầu vòng lặp để hiển thị menu và thực hiện các chức năng
        print("\n1. Thêm từ mới")
        print("2. Xóa từ")
        print("3. Tra cứu nghĩa của từ")
        print("4. In từ điển")
        print("5. Lưu và thoát")
        choice = int(input("Chọn: "))  # Chờ người dùng chọn chức năng cần sử dụng

        if choice == 1:
            add_word(dictionary)  # Gọi hàm để thêm từ mới
        elif choice == 2:
            remove_word(dictionary)  # Gọi hàm để xóa từ
        elif choice == 3:
            lookup_word(dictionary)  # Gọi hàm để tra cứu nghĩa của từ
        elif choice == 4:
            print_dictionary(dictionary)  # Gọi hàm để in từ điển ra màn hình
        elif choice == 5:
            save_dictionary(dictionary, filename)  # Gọi hàm để lưu từ điển và kết thúc chương trình
            print("Từ điển đã được lưu.")
            break  # Kết thúc vòng lặp và chương trình
        else:
            print("Lựa chọn không hợp lệ.")  # Thông báo nếu lựa chọn không hợp lệ

if __name__ == "__main__":  # Kiểm tra nếu chương trình được chạy trực tiếp từ Python
    main()  # Gọi hàm main để chạy chương trình