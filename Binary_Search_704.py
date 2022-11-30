def binary_search(arr,target):
    low=0
    high =len(arr)-1
    
    
    while(low <= high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return(mid)
        elif(arr[mid]<target):
            low = mid+1
        else:
            high = mid-1
    return -1
            

arr = [-1,0,3,5,9,12]
target = 9
binary_search(arr,target)
