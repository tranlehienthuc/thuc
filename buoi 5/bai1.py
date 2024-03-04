import random

city_names = ['paris', 'london', 'berlin', 'madrid']# Danh sách tên thành phố

city_temps = {city: random.randint(20, 30) for city in city_names}# Tạo từ điển với thành phố là khóa và nhiệt độ ngẫu nhiên
print(city_temps)

above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}# Tạo từ điển mới với các thành phố có nhiệt độ lớn hơn 25 độ C
print(above_25)
