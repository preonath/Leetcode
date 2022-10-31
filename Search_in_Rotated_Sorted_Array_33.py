def search(nums,target):
    index = 0  
    if(target not in nums):
        return(-1)
    for i in nums:
        if(i == target):
            return(index)

        index+=1
        
        
nums = [4,5,6,7,0,1,2]
target = 0
search(nums,target)
