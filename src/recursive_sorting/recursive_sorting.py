

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # Your code here

    # divide
    mid = int(len(arr) / 2) 
    left = arr[:mid]
    right = arr[mid:]
    
    #iterators for left and right 
    i = 0 # left
    k = 0 # right
    p = 0 # main
    
    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            # The value from the left half has been used
            arr[p] = left[i]
            # Move the iterator forward
            i += 1
        else:
            arr[p] = right[p]
            p += 1
        
        # Move to the next slot
        p += 1

        # For all the remaining values
    while i < len(left):
        arr[p] = left[i]
        i += 1
        p += 1

    while p < len(right):
        arr[p]=right[p]
        p += 1
        p += 1

        
    
    
    
    
    
 


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr



print(merge_sort([5,3,2,1,9]))