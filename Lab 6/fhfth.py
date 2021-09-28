def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n

while True:
    n = int(input())
    if n==-1:
        break
    print(sum(n))
