def isPerm(s1, s2):
    if len(s1) != len(s2):  # aabc caba
        return False
    counts = {}
    for elem in s1:
        if elem in counts:  # a:1 b:1 c:1
            counts[elem] += 1
        else:
            counts[elem] = 1
    for elem in s2:
        if elem in counts:
            counts[elem] -= 1
            if counts[elem] == 0:
                counts.pop(elem)
        else:
            return False

    return True


print(isPerm('jklye', 'oyjkl'))
