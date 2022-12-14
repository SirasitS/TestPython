def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    num_indices = {}
    for i, num in enumerate(numbers):
        if target_sum - num in num_indices:
            return (num_indices[target_sum - num], i)
        else:
            num_indices[num] = i

    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))