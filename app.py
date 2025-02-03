def longest_increasing_decreasing_subarray(arr):
    if not arr:
        return 0, []

    n = len(arr)
    max_length = 1
    inc_length = 1
    dec_length = 1
    start_index = 0
    max_start_index = 0
    is_increasing = True
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc_length += 1
            dec_length = 1
            if inc_length == 2:
                start_index = i - 1
            if inc_length > max_length:
                max_length = inc_length
                max_start_index = start_index
                is_increasing = True
        elif arr[i] < arr[i - 1]:
            dec_length += 1
            inc_length = 1
            if dec_length == 2:
                start_index = i - 1
            if dec_length > max_length:
                max_length = dec_length
                max_start_index = start_index
                is_increasing = False
        else:
            inc_length = 1
            dec_length = 1

    longest_subarray = arr[max_start_index:max_start_index + max_length]
    return max_length, longest_subarray

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 5, 3, 4, 5, 6, 2, 1, 0, -1]
    length, subarray = longest_increasing_decreasing_subarray(arr)
    print(f"The length of the longest strictly increasing or decreasing subarray is: {length}")
    print(f"The longest subarray is: {subarray}")