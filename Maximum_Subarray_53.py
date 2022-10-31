### K-mer approch ###

nums=[-2,1,-3,4,-1,2,1,-5,4]
# nums=[5,4,-1,7,8]
def Maximum_Subarray(nums):
    min_len_of_k_mer = 1
    max_len_of_k_mer = len(nums)+1
    maximum_values_of_all_k_mer=[]
    for k in range(min_len_of_k_mer, max_len_of_k_mer):
        res = []
        for i in range(len(nums)-k+1):
            k_mer = nums[i:i+k]
            res.append(sum(k_mer))
        all_k_mers = max(res)
        maximum_values_of_all_k_mer.append(all_k_mers)
    return(max(maximum_values_of_all_k_mer))
Maximum_Subarray(nums)


### Dynamic problem Solution ####

## Kadane’s Algorithm ##

#https://www.youtube.com/watch?v=_Nj_3FvGpZU&t=1183s #


def Maximum_Subarray(nums):
    if max(nums) < 0:
        return max(nums)
    global_maximum= nums[0]
    current_sum=nums[0]

    for i in nums[1:]:
        current_sum = max(current_sum+i,i)
        global_maximum=max(global_maximum,current_sum)
    return(global_maximum)

nums=[-2,1,-3,4,-1,2,1,-5,4]
Maximum_Subarray(nums)
