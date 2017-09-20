'''
Decoding function:
After the neural network training, there must be a way of converting a vector of wickelfeatures into wickelphones again and, finally,
back to a whole string (verb).
'''
##############################################################################################################################################################

# '''
# First of all, I need a text file containing a list of verbs
# #not sure about this
# '''
#
# import pickle
# with open("list_verbs.txt", "rb") as file:
#     list_verbs = pickle.load(file)
##############################################################################################################################################################
# '''
# Wickelphone_list:
# Creating a SET of wickelphones given a list of verbs.
# This procedure must create a list (a set) of all existing wickelphones in this verb list.
# '''
#
# import coding_function as cf
#
# def wickelphone_list (list_verbs):
#     wklphone_list = []
#     for item in list_verbs:
#         wklphone_list.append(cf.trigramizer(item))
#     return wklphone_list
#
# wickelphone_list(list_verbs)
from itertools import compress
import coding_function as cf

dar = cf.coding("#dar#")
Dar = cf.vector2string(dar,wickelfeatures_list)
Dar


def checkcandidates(wickelfeatures_list):
    #first = []

    for item in wickelfeatures_list:
        if item[0] == "#":
            first.append(item[1])
    for item in first:
        if 'int' in item:
            print('d')

    pass

checkcandidates(Dar)

class MyList(list):
    def __init__(self, *args):
        super(MyList, self).__init__(args)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])

candidates = MyList('b','p','d','t','g',
              'k','m','n','v','f','z','s',
              'j','x','l','r','a','e','E',
              'i', 'o', 'O', 'u')

ints = MyList('b','p','d','t','g','k','m','n')
conts = MyList('v','f','z','s','j','x','l','r')
vowels = MyList('a','e','E','i', 'o', 'O', 'u')
b1s = MyList('b','p','d','t','g','k','v','f','z','s','j','x','E','i','O','u')
b2s = MyList('m','n','l','r','a','e','o')
fronts = MyList('b','p','v','f','m','l','E','i','e')
middles = MyList('d','t','n','z','s','r','a')
backs = MyList('g','k','j','x','o', 'O', 'u')
d1s = MyList('b','d','g','m','v','z','j','l','o','n','r','e')
d2s = MyList('p', 't', 'k', 'f', 's', 'x', 'a', 'E', 'i', 'O', 'u')
