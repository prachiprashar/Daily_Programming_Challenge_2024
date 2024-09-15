def trap_rain_water(height):
    if not height:
        return 0
    
    left =0
    right = len(height) - 1
    left_max =0
    right_max = 0
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water

# Test cases
print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  
print(trap_rain_water([4, 2, 0, 3, 2, 5]))                      
print(trap_rain_water([1, 1, 1]))                               
print(trap_rain_water([5]))                                     
print(trap_rain_water([2, 0, 2]))                              
