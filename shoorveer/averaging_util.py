from chitragupta import historical_data_wrapper, historical_data_ops, averaging_util_wrapper
from shoorveer import satya, dukaandaar, shakuntala
from shoorveer.continuity import disable_new_buy

buy_amount = 10000
logging = "debug"
first_sell_amount = 10000
PERCENTAGE_ROLL_OVER = 0.8

def get_stocks_to_load():
    return satya.read_nifty_50()


def run():
    for holding in dukaandaar.get_holdings():
        denominator = holding['quantity'] * holding['average_price']
        if denominator != 0:
            percentage_diff = (holding['pnl'] * 100) / (holding['quantity'] * holding['average_price'])
            symbol = holding['tradingsymbol']
            if holding['tradingsymbol'] in get_stocks_to_load() and holding['day_change_percentage']>0:
                print(symbol, " ", percentage_diff)
                if percentage_diff > 2:
                    # SELL
                    last_data = averaging_util_wrapper.get(symbol)
                    if len(last_data) < 1:
                        last_price = dukaandaar.price(symbol)
                        quantity = max(int(int(first_sell_amount) / last_price), 1)
                        data = {'action': 'sell', 'price': last_price, 'quantity': quantity}
                        averaging_util_wrapper.put(symbol, data)
                        dukaandaar.execute_sell_order(symbol, min(quantity, holding['realised_quantity']),
                                                      last_price)
                        continue
                    last_price = dukaandaar.price(symbol)
                    diff_with_last_sold = shakuntala.calculate_percentage_difference(last_data['price'], last_price)
                    if diff_with_last_sold < -1 * PERCENTAGE_ROLL_OVER:
                        quantity = last_data['quantity'] * 2
                        data = {'action': 'sell', 'price': last_price, 'quantity': quantity}
                        averaging_util_wrapper.put(symbol, data)
                        dukaandaar.execute_sell_order(symbol, min(quantity, holding['realised_quantity']),
                                                      last_price)



# while True:
# run()
#     sleep(100)
