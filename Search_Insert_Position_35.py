def insert_position(nums,target):
    low=0
    high =len(nums)-1
    
    while(low<=high):

        mid=(low+high)//2
        if(nums[mid]==target):
            return(mid)
        elif(nums[mid]<target):
            low = mid+1
        else:
            high = mid-1
    return low
            

nums = [-1,0,3,5,9,12]
target = 13
insert_position(nums,target)
