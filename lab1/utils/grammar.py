import graphviz
  

class Grammar(object):
    type = "Type 3 : Regular Grammar by Chomsky"


    def __init__(self, vn:list, vt:list, p:dict , s:str):
        """AI is creating summary for __init__

        Args:
            vn (list): [description]
            vt (list): [description]
            p (dict): [description]
            s (str): [description]

        Raises:
            ValueError: If an Arg does not coresponds or args doesn't pass the
            validation
        """
        self.type = "Type 3 : Regular Grammar by Chomsky"
        p_keys = p.keys()
        p_values = p.values()
        
        if s not in vn:
            raise ValueError('s not in vn')
        if vn[0] != s:
            raise ValueError('s is not the first item in vn')
        
        for k_element in p_keys: 
            for vn_element in vn:
                if k_element not in vn or vn_element not in p_keys :
                    raise ValueError(f'Check vn list or p keys')
                else:
                    for v_element in p_values:              
                        for l_element in v_element:  
                            for s_element in list(l_element): 
                                if s_element not in vn and s_element not in vt:
                                    raise(f" {s_element} from {list(l_element)} ")
                                
        self.vn = vn
        self.vt = vt
        self.p = p
        self.s = s
        
    def to_fa(self):
        """

        Returns:
            dict: a Finite Automaton dictionary 
        """
        fa = {}
        q_list = self.vn
        delta = self.p
        
        for element in q_list:
            fa[q_list.index(element)] = {}
            for value in delta[element]:
                try:
                    fa[q_list.index(element)][value[0]]
                except KeyError:
                    fa[q_list.index(element)][value[0]] = []
                try:
                    fa[q_list.index(element)][value[0]].append(q_list.index(value[1]))
                    

                except IndexError as error:
                    fa[q_list.index(element)][value[0]].append(len(q_list))
        return fa

    def is_acceptable(self, string:str) -> bool:
        """AI is creating summary for is_acceptable

        Args:
            string (str): the string to test

        Returns:
            bool: True if the input string is acceptable
        """
        
        transitions=self.to_fa
        initial=self.vn.index(self.s)
        state = initial
        accepting = []
        for element in transitions():
            for key, value in transitions()[element].items():
                if len(self.vn) in value:
                    accepting.append(key)

        
        for c in string:
            
            if state != len(self.vn) and string.index(c) != len(string) - 1:
                if c in transitions()[state].keys():
                    try:
                        state = transitions()[state][c].remove(len(self.vn))
                    except ValueError:
                        state = transitions()[state][c][0]
                    
                    
                    
                else:
                    return False
            else:
                if c in accepting:
                    # if transitions[state]
                    return True
                else:
                    return False

    def graph(self):
        """
        Output: A png and gv file with the FA Graph in the script directory 
        """
        f = graphviz.Digraph('DFA', filename='dfa.gv')
        f.attr(rankdir="Q", size='8.5')

        f.attr('node', shape='doublecircle')
        f.node(f"q{len(self.vn)}")

        f.attr('node', shape='circle')
        fa = self.to_fa()
        for element in fa:
            for value in fa[element]:
                for i in fa[element][value]:
                    f.edge(
                        f'q{element}',
                        f'q{i}',
                         label=value )
        f.format = 'png'
        f.view(quiet=True)