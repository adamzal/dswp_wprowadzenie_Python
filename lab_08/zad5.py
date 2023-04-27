def top_10_percent(arr):
    arr_sorted = sorted(arr, reverse=True)
    top_count = int(len(arr) * 0.1)
    return arr_sorted[:top_count]