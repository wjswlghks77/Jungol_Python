n = int(input())
for i in range(0, n):
    for j in range(n - 1,i, -1):
        print(end='  ')
    for j in range(0, i + 1):
        print(j + 1, end=' ')
    print()