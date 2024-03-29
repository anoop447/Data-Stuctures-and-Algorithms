
def binary_search(key,arr):

    low = 0
    mid = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high-low) // 2

        if key == arr[mid]:
            return mid

        elif key > arr[mid]:
            low = mid + 1

        elif key < arr[mid]:
            high = mid - 1
            

    return -1


arr = [10,20,22,25,30,33,45,45,50]
print('Enter key to be searched')
key = int(input())

res = binary_search(key,arr)

if res == -1:
    print('Element not found')
else:
    print('Element found at index ' + str(res))


            
