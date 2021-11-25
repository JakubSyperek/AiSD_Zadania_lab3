def n_sums(n):
    c1 = int(str(n)[0])
    c2 = int(str(n)[1])
    c3 = int(str(n)[2])
    if c1 + c3 == c2:
        return True
    else:
        return False

print(n_sums(386))
