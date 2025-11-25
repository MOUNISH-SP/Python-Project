#Fibanocci Series 0 1 1 2 3 5 8 13 21 34 55.........
def fibanocci(n):
  first =0
  second=1
  while n>0:
    third=first+second
    first=second
    second=third
    n-=1
  print(third)

n=int(input("Enter a number: "))
fibanocci(n)

