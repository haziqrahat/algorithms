cache={}
def fibM(n):
  if n<2:
    return n
  else:
    a=cache.get(n-1)
    b=cache.get(n-2)
    if a==None:
      a=fib(n-1)
      cache[n-1]=a
    if b==None:
      b=fib(n-2)
      cache[n-2]=b
    return a+b
