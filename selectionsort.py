def selection_sort(list_a):
    indexing_length = range(0,len(list_a)-1)

    for i in indexing_length:
        min_val = i

        for j in range(i+1,len(list_a)):
            
            if list_a[j] < list_a[min_val]:
                min_val = j
            

        if min_val != i:
            list_a[min_val], list_a[i] = list_a[i], list_a[min_val]

    return list_a

print(selection_sort([2,7,5,6,4,8,9,2,0,6]))
