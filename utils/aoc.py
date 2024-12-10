from ntpath import join
from posixpath import dirname


def add_borders(m, n=1, c='.'):
    m = [n*c + l + n*c for l in m]
    h = n*[len(m[0]) * c]
    return h + m + h

def get_matrix(f):
    return [l[:-1] for l in f.readlines()] 
