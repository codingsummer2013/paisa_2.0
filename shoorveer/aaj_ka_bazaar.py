from datetime import datetime
from time import sleep

from chitragupta import sip_orders_wrapper
from shoorveer import dukaandaar, shakuntala, satya

logging = "debug"


def delete_sip_buy_order_today(symbol):
    sip_order_data = sip_orders_wrapper.get(symbol)
    if len(sip_order_data) >= 1:
        last_available_record = sip_order_data[-1]  # Assign the last element
        last_purchased_date = last_available_record["time"]
        if satya.same_day(datetime.today(), datetime.strptime(last_purchased_date, "%Y-%m-%d")):
            sip_order_data = sip_order_data[:-1]
            sip_orders_wrapper.put(symbol, sip_order_data)


def run():
    positions = dukaandaar.positions()
    for position in positions:
        buy_quantity = position['buy_quantity']
        sell_quantity = position['sell_quantity']
        order_type = None
        quantity = 0
        symbol = position['tradingsymbol']
        current_price = dukaandaar.price(position['tradingsymbol'])
        if buy_quantity > sell_quantity:
            order_type = "BUY"  # the stock has been purchased
            quantity = buy_quantity - sell_quantity
            last_buy_order = dukaandaar.get_maximum_buy_order(symbol)
            if last_buy_order is None:
                continue
            profit = (current_price - last_buy_order['average_price']) * abs(position['quantity'])
            percentage_diff = shakuntala.calculate_percentage_difference(current_price,
                                                                         last_buy_order['price'])
            if logging == "debug":
                print("day change for stock", position['tradingsymbol'], profit, percentage_diff)
            if percentage_diff > 1:
                dukaandaar.execute_sell_order(position['tradingsymbol'], position['quantity'], current_price)
                delete_sip_buy_order_today(position['tradingsymbol'])
        else:
            order_type = "SELL"
            quantity = sell_quantity - buy_quantity
            if quantity == 0:
                continue
            last_sell_order = dukaandaar.get_minimum_sell_order(symbol)
            profit = (last_sell_order['average_price'] - current_price) * abs(position['quantity'])
            percentage_diff = shakuntala.calculate_percentage_difference(last_sell_order['price'],
                                                                         current_price)
            if logging == "debug":
                print("Day change for stock", position['tradingsymbol'], profit, percentage_diff)
            if percentage_diff > 1:
                little_low_price = shakuntala.calculate_99_75_percent(current_price)
                print("Last compared price", current_price, little_low_price)
                dukaandaar.execute_buy_order_with_quantity(position['tradingsymbol'], current_price, quantity)

#
# while True:
#     run()
#     sleep(100)
