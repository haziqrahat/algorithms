def binarySearch(arr,e):
  mid=len(arr)//2
  left=arr[:mid]
  right=arr[mid:]
  if len(arr)==1 and arr[0]!=e:
    return False
  elif arr[mid]==e:
    return True
  elif e>=arr[mid]:
    return binarySearch(right,e)
  else:
    return binarySearch(left,e)
  
