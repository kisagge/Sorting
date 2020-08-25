TC = int(input())   
ans = []
for tc in range(1, TC + 1):
    k = "#"+str(tc) + " "
    # N 입력받기
    n = int(input())

    # N개의 정수를 입력받아 리스트에 지침
    array = []
    for i in range(n):
        array.append(int(input()))
    
    # 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
    array = sorted(array, reverse=True)

    # 정렬이 수행된 결과를 출력
    for i in array:
        k += str(i) + " "
    ans.append(k)
for e in ans:
    print(e)