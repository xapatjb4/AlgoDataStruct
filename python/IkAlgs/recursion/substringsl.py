# same start and end char substring count using divide and conquer
# this leaves us with O(nlogn) time complexity
# O(n) space complexity (if all elements in string are distint)
# submitted this approach to
# https://write.geeksforgeeks.org/improve-post/3120079/
def nsl(s):
    if len(s) == 0:
        return 0
    ma, no = nslh(s, 0, len(s)-1)
    return no


def nslh(s, st, en):
    ma = {}
    if st >= en:
        ma[s[st]] = 1
        return {s[st]: 1}, 1
    mid = (st+en)//2
    mal, sol = nslh(s, st, mid)
    mar, sor = nslh(s, mid+1, en)
    nc = 0
    for x in mal:
        if x in mar:
            nc += mal[x] * mar[x]
    for x in mar:
        if x in mal:
            mal[x] += mar[x]
        else:
            mal[x] = mar[x]
    return mal, nc+sol+sor


print(nsl("abcabbca"))
