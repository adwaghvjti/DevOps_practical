def longest_increasing_decreasing_subarray(arr):
    if not arr:
        return 0
    
    n = len(arr)
    max_length = 1
    inc_length = 1
    dec_length = 1
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc_length += 1
            dec_length = 1
        elif arr[i] < arr[i - 1]:
            dec_length += 1
            inc_length = 1
        else:
            inc_length = 1
            dec_length = 1
        
        max_length = max(max_length, inc_length, dec_length)
    
    return max_length

if __name__ == "__main__":
    arr = [1, 2, 2, 5, 3, 4, 5, 6, 2, 1, 0, -1]
    result = longest_increasing_decreasing_subarray(arr)
    print(f"The length of the longest strictly increasing or decreasing subarray is: {result}")