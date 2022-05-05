from utils.nfa_to_dfa import Nfa

q = ["0", "1", "2", "3", "4"]
epsilon = ["a", "b"]
delta = {
        "0": {'a': ["1"], 'b': []},
        "1": {'a': ["2"], 'b': ["1"]},
        "2": {'a': [], "b": ['2', '3']},
        "3": {'a': ["1"], "b": ['4']},
        '4': {'a': [], 'b': []}
    }
q0 = '0'

test = Nfa(q=q, epsilon = epsilon, delta = delta, q0 = q0)
test.transition_table()
print('\n', test.to_dfa())