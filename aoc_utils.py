def add_borders(m, c = '.'):
    m = [c + l + c for l in m]
    h = [len(m[0]) * c]
    return h + m + h