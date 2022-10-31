### Dynamic problem Solution ####
def maxSubArray(self, nums):
    global_max, local_max = 0, 0
    for x in nums:
        print("Local Max: ",local_max)
        print("Nums Value: ",x)
        print()
        local_max = max(0, local_max + x)
        global_max = max(global_max, local_max)
    return global_max
