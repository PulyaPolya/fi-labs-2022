def get_blocks(y, r):
    Y = []
    n = len(y)
    i = 0
    while True:
        if i + r >= n :
            Y.append(y[i:])
            break
        else:
            Y.append(y[i:i+r])
        i += r
    return Y



