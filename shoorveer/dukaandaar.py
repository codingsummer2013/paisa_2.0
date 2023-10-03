import os
from time import sleep

from kiteconnect import KiteConnect

kite = KiteConnect(api_key="tf77pivddr8pmyin")
directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../veda/request_token.txt')
token = open(filename, "r")
kite.set_access_token(token.readline())


def price(symbol):
    sleep(2)
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
        sleep(2)
    except Exception as e:
        print("Exception in executing order", e)


def execute_buy_order_with_quantity(name, price, quantity):
    try:
        order_id = kite.place_order(tradingsymbol=name,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=quantity,
                                    order_type=kite.ORDER_TYPE_LIMIT,
                                    price=price,
                                    product=kite.PRODUCT_CNC,
                                    variety=kite.VARIETY_REGULAR)
        print("Order placed. ID is: ", order_id, name, price)
        sleep(2)
    except Exception as e:
        print("Exception in executing order", e)


def execute_sell_order(name, quantity, price):
    try:
        order_id = kite.place_order(tradingsymbol=name,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=quantity,
                                    order_type=kite.ORDER_TYPE_LIMIT,
                                    price=price,
                                    product=kite.PRODUCT_CNC,
                                    variety=kite.VARIETY_REGULAR)
        print("Order placed. ID is: {}".format(order_id))
        sleep(2)
    except Exception as e:
        print("Exception in executing order", e)


def positions():
    return kite.positions()['net']


def get_first_buy_order(symbol):
    sleep(2)
    orders = kite.orders()
    last_buy_order = None
    for order in orders:
        if order['transaction_type'] == 'BUY' and order['status'] == 'COMPLETE' and order['tradingsymbol'] == symbol:
            if last_buy_order is None or order['order_timestamp'] < last_buy_order['order_timestamp']:
                last_buy_order = order
    return last_buy_order


def get_last_buy_order(symbol):
    sleep(2)
    orders = kite.orders()
    last_buy_order = None
    for order in orders:
        if order['transaction_type'] == 'BUY' and order['status'] == 'COMPLETE' and order['tradingsymbol'] == symbol:
            if last_buy_order is None or order['order_timestamp'] > last_buy_order['order_timestamp']:
                last_buy_order = order
    return last_buy_order


def get_minimum_buy_order(symbol):
    sleep(2)
    orders = kite.orders()
    minimum_buy_order = None
    for order in orders:
        if order['transaction_type'] == 'BUY' and order['status'] == 'COMPLETE' and order['tradingsymbol'] == symbol:
            if minimum_buy_order is None or order['average_price'] < minimum_buy_order['average_price']:
                minimum_buy_order = order
    return minimum_buy_order


def get_maximum_buy_order(symbol):
    sleep(2)
    orders = kite.orders()
    maximum_buy_order = None
    for order in orders:
        if order['transaction_type'] == 'BUY' and order['status'] == 'COMPLETE' and order['tradingsymbol'] == symbol:
            if maximum_buy_order is None or order['average_price'] > maximum_buy_order['average_price']:
                maximum_buy_order = order
    return maximum_buy_order


def get_last_sell_order(symbol):
    sleep(2)
    orders = kite.orders()
    last_sell_order = None
    for order in orders:
        if order['transaction_type'] == 'SELL' and order['status'] == 'COMPLETE' and order['tradingsymbol'] == symbol:
            if last_sell_order is None or order['order_timestamp'] > last_sell_order['order_timestamp']:
                last_sell_order = order
    return last_sell_order


def get_minimum_sell_order(symbol):
    sleep(2)
    orders = kite.orders()
    minimum_sell_order = None
    for order in orders:
        if order['transaction_type'] == 'SELL' and order['status'] == 'COMPLETE' and order['tradingsymbol'] == symbol:
            if minimum_sell_order is None or order['average_price'] < minimum_sell_order['average_price']:
                minimum_sell_order = order
    return minimum_sell_order


def get_closing_price(symbol):
    sleep(2)
    return kite.quote("NSE:" + symbol)["NSE:" + symbol]['ohlc']['close']

# price("ITC")
