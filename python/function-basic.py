# 定義函式
# 函示內部的程式碼, 若是沒有做函式呼叫, 就不會執行
# def product(n1, n2):
#     # print(n1*n2)
#     return n1*n2


# 呼叫函式
# value = product(3, 4) + product(5,6)
# print(value)
# product(3, 4)
# product(5, 6)

# 程式的包裝
def calculate(max):
    sum = 0
    for n in range(1, max+1):
        sum = sum+n
    print(sum)


calculate(10)
calculate(20)
