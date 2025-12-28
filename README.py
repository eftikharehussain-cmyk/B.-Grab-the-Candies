# B.-Grab-the-Candies
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    mihai = 0
    bianca = 0
    for i in lst:
        if i % 2 == 0:
            mihai += i
        else:
            bianca += i
    if mihai > bianca:
        print("YES")
    else:
        print("NO")
