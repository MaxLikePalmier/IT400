# 有序可變動列表 List
grades = [34, 60, 26, 78, 85]
print(grades[0])
grades[0] = 50  # 把 50 放到列表中的第一個位置\
print(grades)
print(grades[1:4])
grades[1:4] = []  # 連續刪除列表中從編號 1 到 4(不含) 的資料
grades = grades + [30, 35]
length = len(grades)  # 列表長度
print(length)
data = [[3, 4, 5], [6, 7, 8]]
print(data[0][2])
data[0][0:2] = [1, 2]
print(data)  # 結果: [[1, 2, 5], [6, 7, 8]]
# 有序不可變動列表 Tuple
data = (1, 2, 3)
print(data[0:2])
# Tuple 的資料無法更動, 例如: data[0] = 0(錯誤)
# 其餘部分皆與List相同
