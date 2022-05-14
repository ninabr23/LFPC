from utils.grammar import Grammar

vn = ["S", "D", "R", ]
vt = ["a", "b", "c", "d", "f"]
p = {
        "S": ["aS", "bD", "fR"],
        "D": ['cD', 'dR', 'd'],
        "R": ["bR", 'f'],
    }
s = 'S'

test = Grammar(vn=vn, vt=vt, p=p, s=s)
print(test.is_acceptable('aabd'))
# test.graph()
print(test.to_fa())