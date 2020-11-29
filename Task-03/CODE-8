## THE D
#### Code

def display(n):
    st = n // 2
    ld = 1
    for i in range(1, n+1):
        for j in range(1, st+1):
            print ("*", end = '')
        for k in range(1, ld+1):
            print ("D", end = '')
        for l in range(1, st+1):
            print("*", end='')
        print()
        if (i<=n//2):
            st -= 1
            ld += 2
        else:
            st += 1
            ld -= 2
n = int(input())
display(n)
