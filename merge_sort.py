
def merge_sort(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  L1 = []
  R1 = []

  for i in range(n1):
    L1.append(A[p+i-1])
  L1.append('end')

  for j in range(n2):
    R1.append(A[q+j])
  R1.append('end')

  i = 0
  j = 0
  for k in range(r):
    pass

A = [6, 5, 4, 3, 2, 1]

merge_sort(A,1,3,6)