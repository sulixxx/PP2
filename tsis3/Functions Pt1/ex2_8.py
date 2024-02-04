def spy_game(nums):
    for i in range ( len ( nums ) - 2 ) :
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7 :
            return True
        elif nums[i] == 7 and nums[i+1] == 0 and nums[i+2] == 0 :
            return True
        elif nums[i] == 0 and nums[i+1] == 7 and nums[i+2] == 0 :
            return True
    return False

print ( spy_game ([ 0, 0, 7 ]))
print ( spy_game ( [] ) )
print ( spy_game ([ 7, 0, 7, 5, 4, 3, 2, 1 ]))

        