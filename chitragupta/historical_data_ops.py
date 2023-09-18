def calculate_max_price(data):
    if not data:
        return None
    return max(data, key=lambda x: x["price"])["price"]


# Function to calculate the minimum price
def calculate_min_price(data):
    if not data:
        return None
    return min(data, key=lambda x: x["price"])["price"]


# Function to calculate the average price
def calculate_average_price(data):
    if not data:
        return None
    prices = [item["price"] for item in data]
    return sum(prices) / len(prices)
