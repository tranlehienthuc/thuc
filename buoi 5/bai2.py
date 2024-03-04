def count_word_frequency(words):
    word_frequency = {}
    for words in words:
        # Nếu từ đã có trong từ điển, tăng số lần xuất hiện lên 1
        if words in word_frequency :
            word_frequency[words] += 1
        # Nếu từ chưa có trong từ điển, thêm vào với số lần xuất hiện là 1
        else:
            word_frequency[words] = 1
    # In ra màn hình tần suất xuất hiện của các từ
    for words, count in word_frequency .items():
        print(f'{words}: {count}')
# Ví dụ sử dụng
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)
