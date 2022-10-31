### Dynamic programming solution ###

def maxProduct(nums):

    positive = nums[0]
    negative = nums[0]
    result = nums[0]
    for num in nums[1:]:
        positive = max(num, positive * num, negative * num)
        negative =  min(num, positive * num, negative * num)
        result = max(result, positive)
    return result
