from 作业.ShopingCart_购物车 import demo_02网站列表页, demo_01网站详情页

while True:
    num = input("用户操作：1.列表页打开购物车  2.详情页打开购物车：")
    if num=="1":
        demo_02网站列表页.use_shopping_cart()
    elif num=="2":
        demo_01网站详情页.use_shopping_cart()
