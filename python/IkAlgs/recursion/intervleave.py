# def interleaving(A,B):
#   iH(A,0,B,0, [])

# def iH(A, xA, B, xB, ans):
#   if xA == len(A) or xB == len(B): #ABC ACB
#     for x in range(xA, len(A)):
#       ans.append(A[xA]) #BUUUUUUG, should have used x instead
#     for x in range(xB, len(B)):
#       ans.append(B[xB])
#     print(ans) #BUUUUUUUUG, DID not remove what needed to be done#BUUUUUG, printed array not string
#     return
#   ans.append(A[xA])
#   iH(A, xA+1, B, xB, ans)
#   ans.pop()

#   ans.append(B[xB])
#   iH(A, xA, B, xB+1, ans)
#   ans.pop()
def interleaving(A, B):
    iH(A, 0, B, 0, [])


def iH(A, xA, B, xB, ans):
    if xA == len(A) or xB == len(B):  # ABC ACB
        for x in range(xA, len(A)):
            ans.append(A[x])
        for x in range(xB, len(B)):
            ans.append(B[x])
        print("".join(str(e) for e in ans))
        for x in range(xA, len(A)):
            ans.pop()
        for x in range(xB, len(B)):
            ans.pop()

        return
    ans.append(A[xA])
    iH(A, xA+1, B, xB, ans)
    ans.pop()

    ans.append(B[xB])
    iH(A, xA, B, xB+1, ans)
    ans.pop()


interleaving("abc", "acb")
