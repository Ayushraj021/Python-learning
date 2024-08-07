def product_of_values(a, b, c):
    values = [a, b, c]

    # Check for the presence of 7 and its position
    if 7 in values:
        index_of_7 = values.index(7)
        values = values[index_of_7 + 1:]

    # Calculate the product of remaining values
    if not values:  # If no values left after removing 7 and its left values
        return -1
    product = 1
    for value in values:
        product *= value
    return product

# Sample Inputs and Outputs
inputs = [(1, 5, 3), (3, 7, 8), (7, 4, 3), (1, 5, 7)]
for inp in inputs:
    print(f"Input: {inp}, Output: {product_of_values(*inp)}")