from collections import deque


def kStairs(n, k, red):
    if k == 1:
        return 1
    q = deque()
    q.append(1)
    lastRem = 0
    for step in range(1, n+1):
        '''
        The idea behind ans is that
        F(n) = F(n-1) + F(n-2)... F(n-k)
        and we know
        F(n-1) = F(n-2) + F(n-3) + ... + F(n-k-1)
        hence to get the sum of all the values up to F(n-1), we need to remove F(n-k-1)
        therefore
        F(n) = F(n-1) + [F(n-1) - F(n-k-1)]
        '''
        ans = 0
        if step not in red:
            ans = q[-1] + q[-1] - lastRem
        q.append(ans)
        if len(q) > k:
            lastRem = q.popleft()
    return q[-1]

    # 112 k = 2 n =4


'''
1 1 2 35

subtract last removed value from most recent value (this will give sum up to most recent value), add most recent value, that's your sum
'''
print(kStairs(3, 2))
print(kStairs(5, 2))
print(kStairs(3, 3))
print(kStairs(5, 3))
# print(kStairs(45, 2))
print(kStairs(100, 2))
# print(kStairs(1000000, 2))
