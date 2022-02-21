def revRec(s):
    ans = list(s)
    rH(ans, 0)
    return "".join(str(e) for e in ans)


def rH(s, x):
    end = len(s)-1 - x  # The
    if end <= x:
        return
    s[x], s[end] = s[end], s[x]
    rH(s, x+1)


print(revRec("hello my name"))
