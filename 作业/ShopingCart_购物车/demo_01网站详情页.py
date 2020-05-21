from 作业.ShopingCart_购物车 import demo_单例模式


def use_shopping_cart():
    """打开购物车"""
    print("详情页--打开购物车")
    cart = demo_单例模式.Shopping()
    # print(cart)
    cart.total_price+=118
    print(cart.total_price)