import numpy as np
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
m=int(input())
n=int(input())
arr = np.concatenate((nums1, nums2))
new_arr=sorted(arr)
print([i for i in new_arr if i != 0])
