n, count = int(input()), 1

for i in range(0, n):
    for j in range(0, i):
        print(end='  ')
    for j in range(n, i, -1) :
        print(count, end=' ')
        count += 1
    print()