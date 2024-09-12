def merge_two_sorted_arrays(arr1,arr2):
    m = len(arr1)
    n= len(arr2)
    for i in range(m):
        if arr1[i]>arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            arr2.sort()

    
    print(arr1)
    print(arr2)
    

merge_two_sorted_arrays([1, 3, 5], [2, 4, 6])
merge_two_sorted_arrays([10, 12, 14],[1, 3, 5])
merge_two_sorted_arrays([2, 3, 8],[4, 6, 10])
merge_two_sorted_arrays([1],[2])


    
    