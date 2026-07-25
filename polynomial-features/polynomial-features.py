def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    poly = []
    for x in values:
        y = [x**p for p in range(degree + 1)]
        poly.append(y)
    return poly