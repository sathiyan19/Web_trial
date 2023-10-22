a=[10,3,4,7]
x=2
y=3

def solution(a, x, y):
    min_cost = float('inf')  # Initialize with positive infinity

    for i in range(len(a) - (x - 1) * y):
        cost = 0
        for j in range(i, i + x * y, y):
            cost += a[j]

        min_cost = min(min_cost, cost)

    return min_cost

print(solution(a,x,y))