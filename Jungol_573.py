n = int(input())
arr = [[] for _ in range(n)]
count = 1

for i in range(n) :
    for j in range(n):
        print(count, end=' ')
        count += 1
    print()