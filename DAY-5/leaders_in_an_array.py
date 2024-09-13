def find_leaders(arr):
    n = len(arr)
    max_from_right = arr[n-1]
    leaders=[]
    leaders.append(max_from_right)
    for i in range(n-1,-1,-1):
        if  arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    leaders.reverse()
    print(leaders)

find_leaders([16, 17, 4, 3, 5, 2])
find_leaders([1, 2, 3, 4, 0])
find_leaders([7, 10, 4, 10, 6, 5, 2])
find_leaders([100, 50, 20, 10])
list = list(range(1,1000001))
find_leaders(list)