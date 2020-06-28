def unique(l):
  z = []
  for a in l:
    if a not in z:
      z.append(a)
  return z

print(unique([1,2,3,3,3,3,4,5]))