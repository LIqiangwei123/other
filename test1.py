"""
    给定递增数组的初始化元素（大小，间隔，第一个数字），
    构建递增数组
    并通过给定的索引返回递增数组中元素
"""

print("hello world")
size = eval(input("请输入递增数组大小："))
first_number = eval(input("请输入递增数组第一个数字："))
interval = eval(input("请输入递增数组间隔："))
list_a = []
for i in range(size):
    list_a.append(first_number + i * interval)

while True:
    index = eval(input("请输入索引："))
    if index > size or index < 1:
        print("ERROR!!!")
    else:
        print(list_a[index - 1])
        break

print("欢迎下次使用！")
print("thank you")

