# 載入 pandas 模組
import pandas as pd
# 讀取資料
data = pd.read_csv("googleplaystore.csv")  # 把 csv 格式的檔案讀取成一個 DataFrame
# 觀察資料
# print("資料數量", data.shape)
# print("資料欄位", data.columns)
# print("==================")

# # # 分析資料: 評分的各種統計數據
# condition = data["Rating"] <= 5
# data = data[condition]
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得前一百個應用程式的平均", data["Rating"].nlargest(
#     100).mean())  # result--> 取得前一百個應用程式的平均 5.14
# # condition = data["Rating"] > 5

# 分析資料: 安裝數量的各種統計數據
# print(data["Installs"])
# print(data["Installs"][10472])
# ValueError: Unable to parse string "Free" at position 10472
# data["Installs"] = pd.to_numeric(
#     data["Installs"].str.replace("[,+]", "").replace("Free", ""))
# print("平均數", data["Installs"].mean())
# condition = data["Installs"] > 100000
# print("安裝數量大於 1000000 的應用程式有幾個", data[condition].shape[0])

# 基於資料得應用: 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字:")
condition = data["App"].str.contains(keyword, case=False)  # 忽略大小寫
# print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])
