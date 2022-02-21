# from text editor
# def findSpot(n):
#   ans = [0] * 2*n
#   avs = set()
#   avn = set()
#   for x in range(1,n+1):
#     avn.add(x)
#   for x in range(2*n):
#     avs.add(x)
#   fsh(0, ans, avn, avs)

# def fsh(i, ans, avn, avs):
#   if i == len(ans)//2:
#     print("".join(ans)) # bug, joining ints to string
#   avnc = avn.copy()
#   avsc = avs.copy()
#   for num in avnc:
#     for spot in avsc:
#       ans[spot] = num
#       ni = spot+1+num
#       if ni < len(ans): #bug, did not check that new spot was already taken
#         ans[ni] = num
#         avs.remove(spot)
#         avs.remove(ni)
#         avn.remove(num)
#         fsh(i+1, ans, avn, avs)
#         avs.add(spot)
#         avs.add(ni)
#         avn.add(num)
# code was suboptimal, printed many duplicates.... no bueno

def findSpot(n):
    ans = [0] * 2*n
    avs = set()
    avn = set()
    for x in range(1, n+1):
        avn.add(x)
    for x in range(2*n):
        avs.add(x)
    fsh(0, ans, avn, avs)


def fsh(i, ans, avn, avs):
    if i == len(ans)//2:
        print("".join(str(e) for e in ans))
        return
    avnc = avn.copy()
    avsc = avs.copy()
    for num in avnc:
        for spot in avsc:
            ans[spot] = num
            ni = spot+1+num
            if ni < len(ans) and ni in avs:
                ans[ni] = num
                avs.remove(spot)
                avs.remove(ni)
                avn.remove(num)
                fsh(i+1, ans, avn, avs)
                avs.add(spot)
                avs.add(ni)
                avn.add(num)


findSpot(3)
