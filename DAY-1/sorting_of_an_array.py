def sorting_of_array(arr):
    count_zero = 0
    count_one = 0
    count_two = 0
    for num in arr:
        if num == 0:
            count_zero+=1
        elif num == 1:
            count_one+=1
        elif num == 2:
            count_two+=1
        else:
            print("Invalid number!!")
    i = 0
    for num in range(count_zero):
        arr[i] = 0
        i+=1

    for num in range(count_one):
        arr[i] = 1
        i+=1

    for num in range(count_two):
        arr[i] = 2
        i+=1
    print(arr)

sorting_of_array([0, 1, 2, 1, 0, 2, 1, 0])
sorting_of_array([2, 2, 2, 2])
sorting_of_array([0, 0, 0, 0])
sorting_of_array([1, 1, 1, 1])
sorting_of_array([2, 0, 1])
sorting_of_array([])