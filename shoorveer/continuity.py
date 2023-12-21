# Takes last bought price or last day price stored in data. Take minimum of both and do 0.5% less only
# if the order is not executed for the given week
from datetime import datetime
from time import sleep

from chitragupta import sip_orders_wrapper, historical_data_wrapper
from shoorveer import satya, dukaandaar, shakuntala

buy_amount = 5000
logging = "debug"
disable_new_buy = True
force_buy_today = True

def get_stocks_to_load():
    return satya.read_nifty_50()


def run():
    for symbol in get_stocks_to_load():
        sip_order_data = sip_orders_wrapper.get(symbol)
        price_source = None
        price_to_buy = None
        if len(sip_order_data) >= 1:
            last_available_record = sip_order_data[-1]  # Assign the last element
            price_to_buy = last_available_record["price"]
            price_source = "Purchase Source"
            last_purchased_date = last_available_record["time"]
            if satya.same_week(datetime.today(), datetime.strptime(last_purchased_date, "%Y-%m-%d")):
                continue
        market_available_data = historical_data_wrapper.get(symbol)
        if len(market_available_data) >= 1:
            last_available_record = market_available_data[-1]  # Assign the last element
            if price_to_buy is None or price_to_buy > last_available_record["price"]:
                price_to_buy = last_available_record["price"]
                price_source = "Market Source"
        last_price = dukaandaar.price(symbol)
        if force_buy_today:
            price_to_buy = market_available_data[-1]["price"]
        percentage_diff = shakuntala.calculate_percentage_difference(last_price, price_to_buy)
        if logging == "debug":
            print("Percentage diff is", percentage_diff, "for ", symbol)
        if percentage_diff is not None and percentage_diff < -0.2:
            sip_order_info = {'time': datetime.today().strftime("%Y-%m-%d"), 'price': last_price}
            sip_order_data.append(sip_order_info)
            sip_orders_wrapper.put(symbol, sip_order_data)
            if not disable_new_buy:
                dukaandaar.execute_buy_order(symbol, last_price, buy_amount)

#
# while True:
#     run()
#     sleep(100)
