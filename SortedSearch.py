def count_numbers(sorted_list, less_than):
    if sorted_list[-1] < less_than:
        return len(sorted_list)
    if less_than <= sorted_list[0]:
        return 0
    
    # Apply binary search
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        mid = (low + high) // 2   
        if sorted_list[mid] < less_than:
            low = mid + 1
        else:
            high = mid
        
    return len(sorted_list[0:high])




    # return len({result for result in sorted_list if result < less_than})        # Time limit exceed

    # count = 0
    # for val in sorted_list:
    #   if val < less_than:
    #     count += 1;
    #   if val >= less_than:
    #     break
    # return count

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2