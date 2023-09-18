import os

from kiteconnect import KiteConnect

kite = KiteConnect(api_key="tf77pivddr8pmyin")
directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../veda/request_token.txt')
token = open(filename, "r")
kite.set_access_token(token.readline())


def price(symbol):
    return kite.quote("NSE:" + symbol)["NSE:" + symbol]['last_price']


def execute_buy_order(name, price, amount):
    try:
        order_id = kite.place_order(tradingsymbol=name,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=max(int(int(amount) / price), 1),
                                    order_type=kite.ORDER_TYPE_LIMIT,
                                    price=price,
                                    product=kite.PRODUCT_CNC,
                                    variety=kite.VARIETY_REGULAR)
        print("Order placed. ID is: ", order_id, name, price)
    except Exception as e:
        print("Exception in executing order", e)


def execute_sell_order(name, quantity, price):
    order_id = kite.place_order(tradingsymbol=name,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=quantity,
                                    order_type=kite.ORDER_TYPE_LIMIT,
                                    price=price,
                                    product=kite.PRODUCT_CNC,
                                    variety=kite.VARIETY_REGULAR)
    print("Order placed. ID is: {}".format(order_id))


def positions():
    return kite.positions()['net']
