def operation(A,a,cur):
  if a>=0 and A[a]>cur:
    A[a+1] = A[a]
    operation(A,a-1,cur)
  else:
    A[a+1] = cur
    return
def insertion_sort(A):
  for i in range(1, len(A)):
    operation(A, i-1, A[i])
  return

list = [5,2,3,4,1]
insertion_sort(list)
print(list)
