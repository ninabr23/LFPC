import pandas as pd

class Nfa(object):

    def __init__(self, q: list, epsilon: list, delta: dict, q0: str):
        """AI is creating summary for __init__

        Args:
            q (list): [description]
            epsilon (list): [description]
            delta (dict): [description]
            q0 (str): [description]

        Raises:
            ValueError: If an Arg does not coresponds or args doesn't pass the
            validation
        """
        delta_keys = delta.keys()
        delta_values = delta.values()

        if q0 not in q:
            raise ValueError('q0 not in Q')
        if q[0] != q0:
            raise ValueError('q0 is not the first item in Q')

        for k_element in delta_keys:
            for q_element in q:
                if k_element not in q or q_element not in delta_keys:
                    raise ValueError(f'Check vn list or p keys')
                else:
                    for v_element in delta_values:
                        for l_element in v_element:
                            for s_element in list(l_element):
                                if s_element not in q and s_element not in epsilon:
                                    raise(
                                        f" {s_element} from {list(l_element)} ")

        self.q = q
        self.epsilon = epsilon
        self.delta = delta
        self.q0 = q0

    def to_dfa(self):
        """
        Returns:
            dict: a Finite Automaton dictionary 
        """
        nfa = self.delta
        epsilon = self.epsilon
        dfa = {}
        qpr_list = []
        keys_list = list(list(nfa.keys())[0])                #contains all the qs in nfa plus the qs created in dfa are also appended further
        path_list = list(nfa[keys_list[0]].keys())

        # Computing first row of DFA transition table

        dfa[keys_list[0]] = {}                        #creating a nested dictionary in dfa 
        for y in range(len(epsilon)):
            var = "".join(nfa[keys_list[0]][path_list[y]])   #creating a single string from all the elements of the list which is a new state
            dfa[keys_list[0]][path_list[y]] = var            #assigning the q in DFA table
            if var not in keys_list:                         #if the q is newly created 
                if var != "":
                    qpr_list.append(var)                  #then append it to the qpr_list
                keys_list.append(var)    
                
        while len(qpr_list) != 0:                     #condition is true only if the qpr_list is not empty
            dfa[qpr_list[0]] = {}                     #taking the first element of the qpr_list and examining it
            for _ in range(len(qpr_list[0])):
                for i in range(len(path_list)):
                    temp = []                                #creating a temporay list
                    for j in range(len(qpr_list[0])):
                        temp += nfa[qpr_list[0][j]][path_list[i]]  #taking the union of the qs
                    s = ""
                    s = s.join(temp)                         #creating a single string(new q) from all the elements of the list
                    if s not in keys_list:          #if the q is newly created
                        qpr_list.append(s)            #then append it to the qpr_list
                        keys_list.append(s)                  #as well as to the keys_list which contains all the qs
                    dfa[qpr_list[0]][path_list[i]] = s   #assigning the new q in the DFA table
            qpr_list.remove(qpr_list[0])        #Removing the first element in the qpr_list

    
        return dfa


    def transition_table(self):
        """
        Output: A transition table of the DFA 
        """
        dfa = self.to_dfa()
        dfa_table = pd.DataFrame(dfa)

        print(dfa_table.transpose())
