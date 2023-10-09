from chitragupta import historical_data_wrapper, historical_data_ops
from shoorveer import satya, dukaandaar, shakuntala
from shoorveer.continuity import disable_new_buy

percentage_diff_value = 1
buy_amount = 5000
logging = "debug"


def get_stocks_to_load():
    return satya.read_nifty_50()


def run():
    for symbol in get_stocks_to_load():
        historical_data = historical_data_wrapper.get(symbol)
        price_source = "Historical"
        price_to_buy = historical_data_ops.calculate_average_price(historical_data)
        last_order = dukaandaar.get_last_buy_order(symbol)
        if last_order is not None and price_to_buy > last_order["average_price"]:
            price_to_buy = last_order["average_price"]
            price_source = "Today Orders"
        last_price = dukaandaar.price(symbol)
        percentage_diff = shakuntala.calculate_percentage_difference(last_price, price_to_buy)
        if logging == "debug":
            print("Percentage diff is", percentage_diff, "for ", symbol)
        if percentage_diff is not None and percentage_diff < -1 * percentage_diff_value\
                and dukaandaar.get_closing_price(symbol) > last_price:
            little_low_price = shakuntala.calculate_99_75_percent(last_price)
            print("Last compared price", last_price, little_low_price)
            if not disable_new_buy:
                dukaandaar.execute_buy_order(symbol, last_price, buy_amount)

# while True:
#     run()
#     sleep(100)
