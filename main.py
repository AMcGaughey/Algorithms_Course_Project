# ------------ALYSSA MCGAUGHEY------------
# -----------CSC413 ALGORITHMS-----------
# ------------30 NOVEMBER 2025------------

#python program to count inversions in an array(from a file)

import time  # to track runtime

# read array from file
with open("IntegerArray.txt", "r") as file:
    arr = [int(line.strip()) for line in file]
n = len(arr)

# function to use Inversion Count
def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)

# function using merge sort to count inversions
def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0  # used to store inversion counts

    if left < right:
        mid = (left + right) // 2  # divide the array using mid

        inv_count += _mergeSort(arr, temp_arr, left, mid)       # left subarray
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)  # right subarray
        inv_count += merge(arr, temp_arr, left, mid, right)     # merge step

    return inv_count

# merges the subarrays into a sorted array
def merge(arr, temp_arr, left, mid, right):

    i = left     # starting index of left subarray
    j = mid + 1  # starting index of right subarray
    k = left     # starting index of temp array
    inv_count = 0

    # merge the two subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # left subarray remaining elements
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # right subarray remaining elements
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # copy sorted temp_arr back into original array
    for x in range(left, right + 1):
        arr[x] = temp_arr[x]

    return inv_count  # <-- REQUIRED (this was missing)

# measure runtime
start_time = time.perf_counter()
result = mergeSort(arr, n)
end_time = time.perf_counter()

# outputs
print("Inversions:", result)
print("Runtime:", end_time - start_time, "seconds")

# save output
with open("output.txt", "w") as out:
    for num in arr:
        out.write(str(num) + "\n")

print("Sorted Array Saved")
