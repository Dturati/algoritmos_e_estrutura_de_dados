def merge(A,p,q,r):
  n1 = q - p + 1
  n2 = r - q
  L = []
  R = []

  for i in range(n1):
    L.append(A[p+i-1])
  
  for j in range(n2):
    R.append(A[q+j])
 
  i = 0
  j = 0

  for k in range(p-1,r):
    if j >= len(R):
      A[k] = L[i]
      i = i + 1
      continue

    if i >= len(L):
      A[k] = R[j]
      j = j + 1
      continue

    if L[i] <= R[j]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1


A = [6, 5, 4, 3, 2, 1,0, -1, -2, -3]
r = len(A)
def merge_sort(A, p, r):
  if p < r:
    q = int((p+r)/2)
    merge_sort(A,p,q)
    merge_sort(A,q+1,r)
    merge(A,p,q,r)
res = merge_sort(A,1,r)

print(A)