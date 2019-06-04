# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # looping through a second time for comparing int of smallest index to int of other indices
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)):
        # cur_index = i
        print("loop 1", i)
        #comparing int of indexes in pairs then swapping the smaller number to the left side
        # need to only compare with the next index and then move on 
        # for j in range(i+1,):
        #     if arr[j] < arr[i]:
        #         arr[i], arr[j] = arr[j], arr[i]
        #     print("loop 2", j)
        for j in range(len(arr)-i-1):
            print(j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr