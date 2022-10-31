def third_maximum_number(nums):
    
    remove_duplicate = set(nums)
    nums = list( remove_duplicate)
    
    if(len(nums) == 2):
        m = sorted(nums)
        return(m[-1])
    elif(len(nums) < 2):
        return(nums[0])
    else:
        m = sorted(nums) 
        return(m[-3])
nums = [1,1,1]
# nums = [1,2]
# nums = [3,2,1]
# nums = [1,2]
# nums = [2,2,3,1]
third_maximum_number(nums)
