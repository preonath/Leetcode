#Leetcode problem No 
def palindrom(s):
    if(s<0):
        return(False)
    b=int(str(s)[::-1])
    if(b==s):
        return(True)
s=int(input())
palindrom(s)
