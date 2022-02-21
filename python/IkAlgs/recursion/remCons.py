def noCons(n):
    ans = []
    noConsH(n, ans, 0, "")
    return "".join(str(e) for e in ans)


def noConsH(n, ans, i, lch):  # AAABC
    if i == len(n):
        return
    if n[i] != lch:
        ans.append(n[i])
    noConsH(n, ans, i+1, n[i])


print(noCons("AABBBCDDD"))
