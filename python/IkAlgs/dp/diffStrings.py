def diffBetweenTwoStrings(source, target):
    """
    @param source: str
    @param target: str
    @return: str[]
    """
    S = len(source)
    T = len(target)
    sol = [[None for _ in range(T+1)] for _ in range(S+1)]

    s_sol = []
    for x in range(S+1):  # aa  "" a  aa
        sol[x][0] = s_sol[:]
        if x < S:
            s_sol.append("-" + source[x])
    s_sol = []
    for x in range(T+1):
        sol[0][x] = s_sol[:]
        if x < T:
            s_sol.append("+" + target[x])
    print(sol)

    # sol_st = dif_rec(source, S, target, T, sol)
    sol_st = tab(source, target, sol)
    print(sol)
    return sol_st


def dif_rec(source, i_s, target, i_t, sol):
    if sol[i_s][i_t] != None:
        return sol[i_s][i_t][:]
    if source[i_s-1] == target[i_t-1]:
        ans = dif_rec(source, i_s-1, target, i_t-1, sol)
        ans.append(source[i_s-1])
        sol[i_s][i_t] = ans
    else:
        # remove
        rem = dif_rec(source, i_s-1, target, i_t, sol)
        rem.append("-" + source[i_s-1])
        print("rem is")
        print(rem)
        # add
        add = dif_rec(source, i_s, target, i_t-1, sol)
        add.append("+" + target[i_t-1])
        print("add is")
        print(add)

        if len(add) <= len(rem):
            sol[i_s][i_t] = add
        else:
            sol[i_s][i_t] = rem

    return sol[i_s][i_t][:]


def tab(source, target, sol):
    for x in range(1, len(source) + 1):
        for y in range(1, len(target) + 1):
            if source[x-1] == target[y-1]:
                sol[x][y] = sol[x-1][y-1] + list(source[x-1])
            else:
                rem = sol[x-1][y].copy()
                rem.append("-" + source[x-1])
                add = sol[x][y-1].copy()
                add.append("+" + target[y-1])
                if len(add) <= len(rem):
                    sol[x][y] = add
                else:
                    sol[x][y] = rem
    return sol[-1][-1]


print(diffBetweenTwoStrings("ABCDEFG", "ABDFFGH"))
