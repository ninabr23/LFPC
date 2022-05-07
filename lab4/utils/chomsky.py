

class Chomsky(object):

    def __init__(self, vn: list, vt: list, p: dict, s: str):
        """AI is creating summary for __init__

        Args:
            vn (list): nonterminal symbols
            vt (list): terminal symbols
            p (dict): productions
            s (str): starting symbol
        """

        self.vn = vn
        self.vt = vt
        self.p = p
        self.s = s

    def eps_productions(self):
        
        p = self.p

        items_to_remove = []
        for key in p:
            for item in p[key]:
                if item == 'eps':
                    items_to_remove.append(key)
        for item in items_to_remove:
            del p[item]
        for key in p:
            for item in p[key]:
                for itr in items_to_remove: #itr - item  to remove
                    if itr in item: #item - each element for the key's list
                        ita = item.replace(itr,'')
                        p[key].append(ita)
 
        return p

    def elimination_renaming(self):

        p = self.eps_productions()
        vn = self.vn

        items_to_remove = []
        for key in p:
            for item in p[key]:
                for vns in vn:   
                    # valorile de la cheia pe care o stergam o adaugam la cheia actuala
                    if len(item) == 1 and vns in item: 
                        items_to_remove.append(item)
                        for x in p[item]:
                            p[key].append(x)

        for key in p: # elimination of renaming 
            for item in p[key]:
                for itr in items_to_remove:  
                    if itr in p[key]:
                        p[key].remove(itr)      
        return p

    def nonprod_symbols(self):
        p = self.elimination_renaming()
        values_to_remove = []
        vn = self.vn
        for key in p:
            for value in p[key]:
                for letter in value:
                    if letter not in p.keys() and letter not in self.vt:
                        values_to_remove.append(value)
                        try:
                            vn.remove(letter)
                        except:
                            pass
        for key in p:
            for value in p[key]:
                for vtr in values_to_remove:
                    try:
                        p[key].remove(vtr)
                    except:
                        pass
        self.new_vn = vn
        return p

    def inacces_symbols(self):
        p = self.nonprod_symbols()
        vn = self.new_vn
        testing_list = []
        value_to_remove = []

        for key in p:
            for value in p[key]:
                for letter in value:
                    testing_list.append(letter)
        for key in p:
            if key not in testing_list:
                value_to_remove.append(key)
        for item in value_to_remove:
            del p[item]
            try:
                vn.remove(item)
            except:
                pass
        self.new_vn = vn
        return p

    def chomsky_form(self):
        p = self.inacces_symbols()
        vn = self.new_vn
        vt = self.vt
        terminal_symbols = ['N', 'M', 'O']
        complex_symbols = ['G', 'V', 'X', 'Y', 'Z']

        assigned_term_symbols = {}
        assigned_complex_symbols = {}

        for key in p:
            cache = []
            for value in p[key]:
                
                if len(value) == 2 and value[0] in vt:
                    if value[0] in assigned_term_symbols.keys():
                        cache.append(assigned_term_symbols[value[0]] + value[1:])
                    else:
                        assigned_term_symbols[value[0]] = terminal_symbols[0]
                        del terminal_symbols[0]
                        cache.append(assigned_term_symbols[value[0]] + value[1:])
                elif len(value) > 2 and value[0] in vt:
                    if value[0] in assigned_term_symbols.keys():
                        if value[1:] in assigned_complex_symbols.keys():
                            temp = assigned_term_symbols[value[0]]+assigned_complex_symbols[value[1:]]
                            cache.append(temp)
                            
                        else:
                            assigned_complex_symbols[value[1:]] = complex_symbols[0]
                            del complex_symbols[0]
                            temp = assigned_term_symbols[value[0]]+assigned_complex_symbols[value[1:]]
                            cache.append(temp)

                    else:
                        if value[1:] in assigned_complex_symbols.keys():
                            assigned_term_symbols[value[0]] = terminal_symbols[0]
                            del terminal_symbols[0]
                            temp = assigned_term_symbols[value[0]]+assigned_complex_symbols[value[1:]]
                            cache.append(temp)
                            
                        else:
                            assigned_term_symbols[value[0]] = terminal_symbols[0]
                            del terminal_symbols[0]
                            assigned_complex_symbols[value[1:]] = complex_symbols[0]
                            del complex_symbols[0]
                            temp = assigned_term_symbols[value[0]]+assigned_complex_symbols[value[1:]]
                            cache.append(temp)
                elif len(value) == 1:
                    cache.append(value)          
            p[key] = cache
        for key in assigned_term_symbols:
            p[assigned_term_symbols[key]] = [key]
        print(assigned_complex_symbols)
        for key in assigned_complex_symbols:
            keys_to_change = []
            if len(key) > 2:
                keys_to_change.append(key)
        print(keys_to_change)

        for key in keys_to_change:
            temp = key
            while len(temp) > 2:

                if temp[0] not in assigned_term_symbols.keys():
                    assigned_complex_symbols[complex_symbols[0]] = temp[1:]
                    p[assigned_complex_symbols[temp]] = [temp[0] + complex_symbols[0]]
                    temp = temp[1:]
                    assigned_complex_symbols[temp] = complex_symbols[0]
                    del complex_symbols[0]
                else:
                    assigned_complex_symbols[complex_symbols[0]] = temp[1:]
                    p[assigned_complex_symbols[temp]] = [assigned_term_symbols[temp[0]] + complex_symbols[0]]
                    temp = temp[1:]
                    assigned_complex_symbols[temp] = complex_symbols[0]
                    del complex_symbols[0]
            if len(temp) == 2:
                p[assigned_complex_symbols[temp]] = [temp]
                del complex_symbols[0]
        for key in p.keys():
            if key not in vn:
                vn.append(key)
        res = {
            "p":p,
            "vn":vn,
        }  
        return res

