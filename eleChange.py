TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(l):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    k += str(sum(a))
    ans.append(k)
for e in ans:
    print(e)