def run():
    n = int(input())
    ans = []
    ans.append(n)
    while n!=1:
        if n%2 == 0:
            n = n // 2
        else:
            n = (n*3) + 1
        ans.append(n)

    for elm in ans:
        print(elm, end=" ")
    
run()