def solve(n):
    if n % 2 == 1:
        return n-1
    else:
        return solve(int(n/2)) + 1
n = int(input())
print(solve(n))

