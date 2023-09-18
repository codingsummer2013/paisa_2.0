from datetime import datetime

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
        if buy_quantity > sell_quantity:
            order_type = "BUY"  # the stock has been purchased
            quantity = buy_quantity - sell_quantity
            profit = (position['last_price'] - position['average_price']) * position['quantity']
            percentage_diff = shakuntala.calculate_percentage_difference(position['last_price'],
                                                                         position['average_price'])
            if logging == "debug":
                print("Position change for stock", position['tradingsymbol'], profit, percentage_diff)
            if percentage_diff > 0.5:
                dukaandaar.execute_sell_order(position['tradingsymbol'], position['quantity'], position['last_price'])
                delete_sip_buy_order_today(position['tradingsymbol'])
        else:
            order_type = "SELL"
            quantity = sell_quantity - buy_quantity
            profit = (position['average_price'] - position['last_price']) * position['quantity']
            percentage_diff = shakuntala.calculate_percentage_difference(position['average_price'],
                                                                         position['last_price'])
            if logging == "debug":
                print("Day change for stock", position['tradingsymbol'], profit, percentage_diff)
            if percentage_diff > 0.5:
                dukaandaar.execute_buy_order(position['tradingsymbol'], position['quantity'], position['last_price'])

# while True:
#     run()
#     sleep(100)
