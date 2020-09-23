def insertionSort(arr):

    length = range(1,len(arr))

    for i in length:
        value_to_sort = arr[i]

        while i>0 and arr[i-1] > value_to_sort:
            arr[i-1],arr[i] = arr[i],arr[i-1]
            i-=1

    return arr

print(insertionSort([2,1,5,7,3,1,4,1,3,6,8,2]))
