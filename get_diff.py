def get_diff(p1, p2):
    if p1 == p2:
        diff = 0
    elif p1>p2:
        diff = p1 - p2
    elif p2 > p1:
        diff = p2 - p1
    return diff