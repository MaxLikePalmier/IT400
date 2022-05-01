# 載入 pandas 模組
import pandas as pd
# 篩選練習 - Series
# data = pd.Series([30, 15, 20])
# condition = [True, False, True]
# condition = data > 18
# print(condition)
# fiilteredData = data[condition]
# print(fiilteredData)

# data = pd.Series(["您好", "Python", "Pandas"])
# condition = data.str.contains("P")
# print(condition)
# fiilteredData = data[condition]
# print(fiilteredData)

# 篩選練習 - DataFrame
data = pd.DataFrame({
    "name": ["Amy", "Bob", "Charles"],
    "salary": [30000, 50000, 40000]
})
# condition = data["salary"] >= 40000
condition = data["name"] == "Amy"
print(condition)
fiilteredData = data[condition]
print(fiilteredData)
