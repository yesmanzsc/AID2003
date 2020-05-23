   列表 list 基础操作
        创建
        追加
        定位
        遍历(循环获取所有元素)
"""
list_furnitures = ["沙发", "饮水机", "衣柜"]
list_furnitures.append("书桌")
list_furnitures.append("椅子")

# 定位  列表名称[整数]
#   获取第一个元素
print(list_furnitures[0])
#   修改第二个元素
list_furnitures[1] = "水壶"
# list_furnitures[4] = "板凳"
list_furnitures[len(list_furnitures) - 1] = "板凳"
print(list_furnitures)
# list_furnitures[8] = "鞋架" # 报错索引越界 IndexError

# 遍历
for item in list_furnitures:
    print(item)

# 修改列表中所有元素(正课讲解)
# for item in list_furnitures:
#     item = ""
