
def romanToInt(self, s: str) -> int:
  dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  pre=0
  total=0
  cur=0
  for i in range(len(s)):
      cur=dict[s[i]]
      if cur>pre:
          total=(total+cur)-(2*pre)
      else:
          total+=cur
      pre=cur
  return total
