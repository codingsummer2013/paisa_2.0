def calculate_percentage_difference(current_price, price_compare):
    # Calculate the absolute difference between the two values
    absolute_difference = (current_price - price_compare)
    # Calculate the percentage difference
    percentage_difference = (absolute_difference / max(current_price, price_compare)) * 100
    return percentage_difference
