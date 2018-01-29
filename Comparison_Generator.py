"""Generates a list of numbers, each powers of two, the highest of which being that which surpsses that value of the
supplied argument, after which the while loop exits. The generated list acts as binary table column headers"
"""
def generate_comparisons(n):
    values = [1]
    while max(values) < n:  # loops - doubling the previous value while the maximum value is less than n
        x = max(values)
        numlist.append(x * 2)
    comparisons = reversed(values)  # list must be reversed in order for comparison operation to work
    return comparisons
