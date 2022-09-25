def bubble(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if arr[j]>arr[j+1]:
        tmp=arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=tmp
  return(arr)
def selection(arr):
    for i in range(len(arr)):
      min=i
      for j in range(i,len(arr)):
        if arr[j]<arr[min]:
          min=j
      tmp=arr[min]
      arr[min]=arr[i]
      arr[i]=tmp
    return(arr)
def insertion(arr):
  for i in range(len(arr)):
    for j in range(i):
      if arr[i]<arr[j]:
        arr.insert(j,arr[i])
        arr.pop(i+1)
        break
  return(arr)
def merge(left,right):
  arr=[]
  lp=0
  rp=0
  while lp <len(left) and rp<len(right):
    if left[lp]<right[rp]:
      arr.append(left[lp])
      lp+=1
    else:
      arr.append(right[rp])
      rp+=1
  while lp<len(left):
    arr.append(left[lp])
    lp+=1
  while rp<len(right):
    arr.append(right[rp])
    rp+=1
  return arr
def mergeSort(arr):
  if len(arr)==1:
    return arr
  else:
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    return merge(mergeSort(left),mergeSort(right))
 def pivot(arr,left,right):
  i=left
  pvt=right
  while i<pvt:
    if arr[i]>arr[pvt]:
      arr[i],arr[pvt-1]=arr[pvt-1],arr[i]
      arr[pvt],arr[pvt-1]=arr[pvt-1],arr[pvt]
      pvt=pvt-1
    else:
      i+=1
  return pvt
def quickSort(arr,start,end):
  if start<end:
    ptr=pivot(arr,start,end)
    quickSort(arr,start,ptr-1)
    quickSort(arr,ptr+1,end)
  return arr
