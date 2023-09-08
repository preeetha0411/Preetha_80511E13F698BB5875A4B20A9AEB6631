def fact_rec(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*fact_rec(n-1)
num=int(input("enter a value:"))
rec=fact_rec(num)
print("the factorial of",num,"is",rec) 