"""购物车 版本1
        业务流程
            死循环：
                1键盘购买/2键盘结算
                    购买过程：
                        显示所有商品
                            格式： 商品编号:xxx,商品名称:xxx,商品单价:xxx.
                        输入商品编号和购买数量创建订单(加入到购物车)
                    结算过程：
                        计算总价格
                        获取金额
                            如果金额 >= 总价格,提示购买成功,清空购物车 list_orders.clear()
                            否则重新获取金额
        实施步骤：
            1. 死循环 --> 1键盘购买 --> 显示所有商品
            2. 创建订单 --> 2键盘结算 --> 显示订单
            3. 画出dict_commoditys、list_orders内存图
            4. 需求：计算总价格
                步骤：
                （1) 获取订单中的商品编号
                （2) 获取商品单价
                （3) 累加商品单价 * 购买数量
            5. 获取金额
                如果金额 >= 总价格,提示购买成功,空购物车 list_orders.clear()
                否则重新获取金额"""
dict_commoditys_shoes  = {
    1001: {"name" : "耐克","price" : 499 },
    1002: {"name": "安踏", "price": 399},
    1003: {"name": "特步", "price": 479},
    1004: {"name": "美特斯邦威", "price": 489},
    1005: {"name": "aj", "price": 400},
    1006: {"name": "阿迪达斯", "price": 398}

}
list_infor_shoes = [
    { "cid" : "1001" , "count" : 30 } ,
    { "cid" : "1002" , "count" : 40 } ,
    { "cid" : "1003" , "count" : 26 } ,
    { "cid" : "1004" , "count" : 18 } ,
    { "cid" : "1005" , "count" : 22 } ,
    { "cid" : "1006" , "count" : 50 }1


]


while True :
    item = input("请输入1键购买2键结算:")
    if item == "1" :
        for cid , dict_info in dict_commoditys_shoes.items() :
            print("商品编号: "+ str(cid)+",商品名称:" + dict_info ["name"]+ ",商品价格:" + str(dict_info["price"]) + "元.")
        info_id = input ("请输入需要购买的商品编号 :")
        info_count =  int(input("请输入需要购买商品的数量："))
        orders =  { "cid" :info_id , "conut" : info_count}
        list_infor_shoes.append(orders)
    if item == "2" :
        total_price = 0
        for orders in list_infor_shoes :
            info_id = orders ["cid"]
            info_price = dict_commoditys_shoes[info_id]["price"]
            total_price += info_price * orders ["count"]
        print("总价格" + str(total_price))
        while True:
            money = float(input("请输入金额"))
            if money >= total_price:
                print("提示购买成功")
                list_infor_shoes.clear()
                break
            else:
                print("金额不足")















