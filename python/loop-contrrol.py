# break 的簡易範例
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) # 印出迴圈中的 n
#     n+=1
# print("最後的 n :", n) # 印出迴圈結束後的 n

# continue 的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # x 是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的 n :", n)

# else 的簡易範例
# sum = 0
# for n in range(11):
#     sum = sum+n
# else:
#     print(sum) # 印出 0+1+2+3+...+10 的結果

# 綜合範例: 找出整數平方根
# 輸入 9, 得到 3
# 輸入 11, 得到【沒有】整數平方根
n = input("輸入一個整數: ")
n = int(n)  # 轉換成數字
for i in range(n):
    if i*i == n:
        print("整數平方根", i)
        break
else:
    print("沒有整數平方根")
