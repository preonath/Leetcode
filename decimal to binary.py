n=int(input())
l=list(bin(n))
l.remove(l[0])
l.remove(l[0])

s=[str(i) for i in l]
m=''.join(s)
print("{}".format(m))
