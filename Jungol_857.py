h, w = map(int, input().split())
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(i * j, end=' ')
    print()