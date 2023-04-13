def dot_product(vector_1, vector_2):
    """Multiplying two vectors by multiplying it's elements. """
    product = 0
    for v, u in zip(vector_1, vector_2):
        product = product + v * u
    return(product)