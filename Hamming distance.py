# a = input("input your string A: ")
# b = input("input your string B: ")
# if len(a) != len(b):
#     print("you must have to enter same length of strings")
# else:
#
#     c = []
#     d = []
#
#     for i in range(0, len(a)):
#         if a[i] != b[i]:
#             d.append(i)
#             c.append(a[i])
#     data = dict(zip(d, c))
#
# print("number of difference:", len(c))
# print("posistion of difference:", d)
# print("The stirngs that are differ:", c)
# print("number wise difference:", data)

# inp1=input('Give the 1st string input: ')
# inp2=input('Give the 2nd string input: ')
# x1=len(inp1)
# mis=[]
# i,j=0,0
# while i<x1:
#     if inp1[i]==inp2[i]:
#         i=i+1
#     else:
#         j=j+1
#         i=i+1
#         mis.append(i)
# print("There are "+str(j)+" mismatch")
# print(mis)
s=input()
n=input()
c = 0
for i,j in zip(s,n):
    if i!=j:
     c+=1
     print(i,end=" ")
print(c)

