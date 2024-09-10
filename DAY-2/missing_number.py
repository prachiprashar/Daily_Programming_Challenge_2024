def find_missing_number(arr):
    sum = 0
    for i in arr:
        sum += i
    n = len(arr)+1
    print((n*(n+1)/2)-sum)

find_missing_number([1, 2, 4, 5])
find_missing_number([2, 3, 4, 5])
find_missing_number([1, 2, 3, 4])
find_missing_number([1])
find_missing_number(list(range(1,1000000)))