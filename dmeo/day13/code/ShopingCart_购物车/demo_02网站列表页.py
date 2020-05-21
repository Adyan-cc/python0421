from ShopingCart_购物车 import demo_单例模式


def use_shopping_cart():
    """打开购物车"""
    print("列表页--打开购物车")
    cart = demo_单例模式.Shopping()
    # print(cart)
    print(cart.total_price)