# def getCombosToSum(n):
#   gch(n,0,[],1)

# def gch(n, cs, slt, min):
#   if n == cs; #bug semicolon instead of colon
#     print(slt)
#     return
#   for x in range(min, n+1):
#     if cs + x <= n:
#       slt.append(x)
#       gch(n, cs+x, slt,x)
#       slt.pop()
#     else:
#       break
def getCombosToSum(n):
    gch(n, 0, [], 1)


def gch(n, cs, slt, min):
    if n == cs:
        print(slt)
        return
    for x in range(min, n+1):
        if cs + x <= n:
            slt.append(x)
            gch(n, cs+x, slt, x)
            slt.pop()
        else:
            break


getCombosToSum(5)
