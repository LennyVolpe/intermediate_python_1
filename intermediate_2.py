

def get_combined_dict(a, b):
     comb_dict = {}
     for x,value in a.items():
        if x in b.keys():
            comb_dict[x] = value + b[x]
     return comb_dict    




my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
print(get_combined_dict(my_dict_1, my_dict_2))