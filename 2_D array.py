r= int(input())
c = int(input())

matrix = []
for i in range(r):
  row = []
  for j in range(c):
    row.append(0)
  matrix.append(row)

print(matrix)