### Solution One Bruteforce ###

s=list(map(int,input().split(',')))
target=int(input())
for i in range(len(s)):
    for j in range(1,len(s)):
        sum=s[i]+s[j]
        if(sum==target):
            print(i,j)
            
            
### ANother Solution using HashMap
##### https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode ##### Logic from this video

def two_sum(s,t):
    index={}
    for i, value in enumerate(s):
        complement=target-value
        if complement in index:
            return(index[complement],i)
        index[value] = i
    
s=list(map(int,input().split(',')))
target=int(input())
two_sum(s,target)
