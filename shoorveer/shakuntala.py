def calculate_percentage_difference(current_price, price_compare):
    # Calculate the absolute difference between the two values
    absolute_difference = (current_price - price_compare)
    # Calculate the percentage difference
    percentage_difference = (absolute_difference / max(current_price, price_compare)) * 100
    return percentage_difference


def calculate_99_75_percent(value):
    if isinstance(value, (int, float)):
        result = value * 0.9975  # 99.75% expressed as a decimal
        result = round(result, 2)  # Round to two decimal places
        last_digit = int(result * 100) % 10  # Extract the last digit
        if last_digit == 0 or last_digit == 5:
            return result
        else:
            # Adjust the result to have the second decimal as 0 or 5
            if last_digit < 5:
                return round(result - (last_digit / 100), 2)
            else:
                return round(result + (5 - (last_digit / 100)), 2)
    else:
        raise ValueError("Input must be a numeric value (int or float)")