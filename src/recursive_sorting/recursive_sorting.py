# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    
    # TO-DO

    for i in range(elements):
        if a == len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
            continue
        if b == len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
            continue
        if arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # divide and conquer

    if len(arr) == 1:
        return arr
    #divides the array in half and will repeat loop to divide arrays until only len of 1 is left
    middle = len(arr) / 2
    #splits left side of array and break it down again until only one element
    left = merge_sort(arr[:middle])
    #splits right side of array and break it down again until only one element
    right = merge_sort(arr[middle:])

    #merges each element after being sorted
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
