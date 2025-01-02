from os.path import join, dirname
from flpc import compile, fmatch

with open(join(dirname(__file__), "input.txt")) as f:
    towels, _, *designs = (l[:-1] for l in f.readlines())
    p = r"^(?:" + r"|".join(towels.split(", ")) + r")+$"
    print(sum(1 for l in designs if fmatch(compile(p), l)))
