def merge(p, q, r, v):
  i = p
  j = q
  k = 0
  w = [0 for r in range(len(v))]
  
  while(i < q and j < r):
    if (v[i] < v[j]):
      w[k] = v[i]
      i = i + 1
    else:
      w[k] = v[j]
      j = j + 1
    k = k + 1

  while(i < q):
    w[k] = v[i]
    i = i + 1
    k = k + 1

  while(j < r):
    w[k] = v[j]
    j = j + 1
    k = k + 1

  for i in range(p,r):
    v[i] = w[i-p]


v = [6, 5, 4, 3, 2, 1]
def merge_sort(p, r, v):
  if p < r-1:
    q = int((p+r)/2)
    merge_sort(p,q,v)
    merge_sort(q,r,v)
    merge(p,q,r,v)
    
merge_sort(0,len(v),v)
print(v)
