import numpy
# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

result=1

for i in nums:
    if(i==0):
        continue
    result*=i

l=[]
for i in nums:
    if(i==0):
        x = result/1
        l.append(x)
    else:
        l.append(result/i)
print(l)
