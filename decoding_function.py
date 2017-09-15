'''
Decoding function:
After the neural network training, there must be a way of converting a vector of wickelfeatures into wickelphones again and, finally,
back to a whole string (verb).
'''
##############################################################################################################################################################
'''
First of all, I need a text file containing a list of verbs
'''

import pickle
with open("list_verbs.txt", "rb") as file:
    list_verbs = pickle.load(file)
##############################################################################################################################################################
'''
Wickelphone_list:
Creating a SET of wickelphones given a list of verbs.
This procedure must create a list (a set) of all existing wickelphones in this verb list.
'''

import coding_function as cf

def wickelphone_list (list_verbs):
    wklphone_list = []
    for item in list_verbs:
        wklphone_list.append(cf.trigramizer(item))
    return wklphone_list

wickelphone_list(list_verbs)
