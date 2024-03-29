def partition(arr, low, high):
    i = (low - 1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller
        # than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quickSort(arr, low, high):
    if low < high:
 pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)
 
if __name__ == '__main__' :
     
    arr = [4, 2, 6, 9, 2]
    n = len(arr)
     
    # Calling quickSort function
    quickSort(arr, 0, n - 1)
     
    for i in range(n):
        print(arr[i], end = " ")