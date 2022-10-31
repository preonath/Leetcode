#### Brute Froce Approch ###

arr = list(map(int,input().split()))
def Contains_Duplicate(arr):
    arr_set=set(arr)
    if len(arr)!=len(arr_set):
        return(True)
    else:
        return(False)
print(Contains_Duplicate(arr))


#### Optimum Solution ###
arr = list(map(int,input().split()))
def containsDuplicate(arr):
    arr_set=set()
    for num in arr:
        if num in arr_set:
            return True
        
        arr_set.add(num)
    else:
        return False
print(containsDuplicate(arr))
