a =input()
b =input()
l =list(bin(int(a,2) + int(b,2)))
l.remove(l[0])
l.remove(l[0])

s=[str(i) for i in l]
m=''.join(s)
print("{}".format(m))


# x = int(input("input your binary number-1: \n"),2)
# y = int(input("input your binary number-2: \n"),2)
# z = bin(x + y)
# print (z)


