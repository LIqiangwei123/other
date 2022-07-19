"""
文件批量重命名
"""


import os

path = "F:\\大三暑假\\暑期社会实践\\实践内容\\特色照片\\"
# 获取该目录下所有文件，存入列表中
f = os.listdir(path)
print(len(f))
print(f[0])

n = 0
i = 0
for i in f:
    # 设置旧文件名（就是路径+文件名）
    old_name = f[n]

    # 设置新文件名
    newname = str(n+1) + '.jpg'
    # 用os模块中的rename方法对文件改名
    os.rename(path + old_name, path + newname)
    print(old_name, '======>', newname)
    n += 1
