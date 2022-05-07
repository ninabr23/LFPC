from utils.chomsky import Chomsky
import json

vn = ["S", "A", "B", "C", "E"]
vt = ["a", "d"]
p = {
        "S": ["dB", "A"],
        "A": ["d", "dS", "aAdAB"],
        "B": ["aC", "aS", "AC"],
        "C": ["eps"],
        "E": ["AS"]
    }
s = 'S'

test = Chomsky(vn=vn, vt=vt, p=p, s=s)
print(f'Elimination of epsilon productions: \n {test.eps_productions()}')
print(f'Elimination of renaming: \n {test.elimination_renaming()}')
print(f'Elimination of nonproductive symbols: \n {test.nonprod_symbols()}')
print(f'Elimination of inaccesible symbols: \n {test.inacces_symbols()}')

print(f"Chomsky Normal Form \n {json.dumps(test.chomsky_form(),indent=2)}")
