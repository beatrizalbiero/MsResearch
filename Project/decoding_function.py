"""
Decoding function.

This Python code will decode a one-hot vector of wickelfeatures back into a
verb after the neural network training.
"""

import coding_function as cf
from Files import nodes

wickelfeatures_list = nodes.nds

"""
idea: start with a set of possible candidates and then reducing them until we
have a winner.
"""


class MyList(list):
    """
    MyList is a new type of list.

    MyList: A new class developed in order to eliminate incompatibilities
    (filtering).

    :MyList type: list
    :rtype: list
    """

    def __init__(self, *args):
        super(MyList, self).__init__(args)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])

###############################################################################


def checkcandidates_beg(vector2string):
    """
    checkcandidates_beg.

    A procedure that decodes the first trigram of a verb.

    :vector2string type: Mylist
    :rtype:
    """
    candidates1 = MyList('b', 'p', 'd', 't', 'g',
                         'k', 'm', 'n', 'v', 'f',
                         'z', 's', 'j', 'x', 'l',
                         'r', 'a', 'e', 'E', 'i',
                         'o', 'O', 'u')
    candidates2 = MyList('b', 'p', 'd', 't', 'g',
                         'k', 'm', 'n', 'v', 'f',
                         'z', 's', 'j', 'x', 'l',
                         'r', 'a', 'e', 'E', 'i',
                         'o', 'O', 'u')

    ints = MyList('b', 'p', 'd', 't', 'g', 'k', 'm', 'n')
    conts = MyList('v', 'f', 'z', 's', 'j', 'x', 'l', 'r')
    vowels = MyList('a', 'e', 'E', 'i', 'o', 'O', 'u')
    b1s = MyList('b', 'p', 'd', 't', 'g', 'k', 'v',
                 'f', 'z', 's', 'j', 'x', 'e', 'i', 'o', 'u')
    b2s = MyList('m', 'n', 'l', 'r', 'a', 'E', 'O')
    fronts = MyList('b', 'p', 'v', 'f', 'm', 'l', 'E', 'i', 'e')
    middles = MyList('d', 't', 'n', 'z', 's', 'r', 'a')
    backs = MyList('g', 'k', 'j', 'x', 'o', 'O', 'u')
    d1s = MyList('b', 'd', 'g', 'm', 'v', 'z', ' j', 'l', 'o', 'n', 'r', 'e')
    d2s = MyList('p', 't', 'k', 'f', 's', 'x', 'a', 'E', 'O', 'u', 'i')

    new = []

    for item in vector2string:
        if item[0] == '#':
            new.append(item)
            if item[1] == 'int':
                # print(candidates)
                candidates1 = candidates1 - conts - vowels
            if item[1] == 'cont':
                candidates1 = candidates1 - ints - vowels
            if item[1] == 'vowel':
                # print(candidates)
                candidates1 = candidates1 - conts - ints
            if item[1] == 'b1':
                # print(candidates)
                candidates1 = candidates1 - b2s
            if item[1] == 'b2':
                # print(candidates)
                candidates1 = candidates1 - b1s
            if item[1] == 'front':
                # print(candidates)
                candidates1 = candidates1 - middles - backs
            if item[1] == 'middle':
                # print(candidates)
                candidates1 = candidates1 - fronts - backs
            if item[1] == 'back':
                # print(candidates)
                candidates1 = candidates1 - fronts - middles
            if item[1] == 'd1':
                # print(candidates)
                candidates1 = candidates1 - d2s
            if item[1] == 'd2':
                # print(candidates)
                candidates1 = candidates1 - d1s
            if item[2] == 'int':
                # print(candidates)
                candidates2 = candidates2 - conts - vowels
            if item[2] == 'cont':
                candidates2 = candidates2 - ints - vowels
            if item[2] == 'vowel':
                # print(candidates)
                candidates2 = candidates2 - conts - ints
            if item[2] == 'b1':
                # print(candidates)
                candidates2 = candidates2 - b2s
            if item[2] == 'b2':
                # print(candidates)
                candidates2 = candidates2 - b1s
            if item[2] == 'front':
                # print(candidates)
                candidates2 = candidates2 - middles - backs
            if item[2] == 'middle':
                # print(candidates)
                candidates2 = candidates2 - fronts - backs
            if item[2] == 'back':
                # print(candidates)
                candidates2 = candidates2 - fronts - middles
            if item[2] == 'd1':
                # print(candidates)
                candidates2 = candidates2 - d2s
            if item[2] == 'd2':
                # print(candidates)
                candidates2 = candidates2 - d1s

    return {'decoded': "".join(['#'] + candidates1 + candidates2),
            'wickelfeatures': new}


'''
Example:
dar = cf.coding('#dar#')
Dar = cf.vector2string(dar)
checkcandidates_beg(Dar)['decoded']
type(checkcandidates_beg(Dar)['decoded'])
'''

'''
find_compatible:
i'm gonna compare the first decoded wickelfeatures with a list of possible new
wickelfeatures, this procedure filters possible candidates for the second
trigram.
'''


def find_compatible(list1, list2):
    """
    Find Compatible.

    returns a list if compatible lists in list2 according to list1

    :list1 type: list
    :list2 type:
    :rtype: list
    """
    compatible = []
    for item1 in list1:
        for item2 in list2:
            if item1[1] == item2[0] and item1[2] == item2[1]:
                compatible.append(item2)

    return compatible
##############################################################################


'''
:
given a set of wickelfeatures, it returns the most likely phoneme
'''


def competition(vector2string, position):
    """
    competition.

    This function will receive a vector2string argument and a position.
    Given this vector2string, phonemes will compete for wickelfeatures.

    :vector2string type: list
    :position type: int
    :rtype: str
    """
    competitors = {'b': 0, 'p': 0, 'd': 0, 't': 0, 'g': 0, 'k': 0, 'm': 0,
                   'n': 0, 'v': 0, 'f': 0, 'z': 0, 's': 0, 'j': 0, 'x': 0,
                   'l': 0, 'r': 0, 'a': 0, 'e': 0, 'E': 0, 'i': 0, 'o': 0,
                   'O': 0, 'u': 0, '#': 0}

    for item in vector2string:
            if item[position] == '#':
                competitors['#'] = competitors['#']+1

            if item[position] == 'int':
                competitors['b'] = competitors['b']+1
                competitors['p'] = competitors['p']+1
                competitors['d'] = competitors['d']+1
                competitors['t'] = competitors['t']+1
                competitors['g'] = competitors['g']+1
                competitors['k'] = competitors['k']+1
                competitors['m'] = competitors['m']+1
                competitors['n'] = competitors['n']+1

            if item[position] == 'cont':
                competitors['v'] = competitors['v']+1
                competitors['f'] = competitors['f']+1
                competitors['z'] = competitors['z']+1
                competitors['s'] = competitors['s']+1
                competitors['j'] = competitors['j']+1
                competitors['x'] = competitors['x']+1
                competitors['l'] = competitors['l']+1
                competitors['r'] = competitors['r']+1

            if item[position] == 'vowel':
                competitors['a'] = competitors['a']+1
                competitors['e'] = competitors['e']+1
                competitors['E'] = competitors['E']+1
                competitors['i'] = competitors['i']+1
                competitors['O'] = competitors['O']+1
                competitors['u'] = competitors['u']+1
                competitors['o'] = competitors['o']+1

            if item[position] == 'b1':
                competitors['b'] = competitors['b']+1
                competitors['p'] = competitors['p']+1
                competitors['d'] = competitors['d']+1
                competitors['t'] = competitors['t']+1
                competitors['g'] = competitors['g']+1
                competitors['k'] = competitors['k']+1
                competitors['v'] = competitors['v']+1
                competitors['f'] = competitors['f']+1
                competitors['z'] = competitors['z']+1
                competitors['s'] = competitors['s']+1
                competitors['j'] = competitors['j']+1
                competitors['x'] = competitors['x']+1
                competitors['e'] = competitors['e']+1
                competitors['i'] = competitors['i']+1
                competitors['u'] = competitors['u']+1
                competitors['o'] = competitors['o']+1

            if item[position] == 'b2':
                competitors['m'] = competitors['m']+1
                competitors['n'] = competitors['n']+1
                competitors['l'] = competitors['l']+1
                competitors['r'] = competitors['r']+1
                competitors['a'] = competitors['a']+1
                competitors['E'] = competitors['E']+1
                competitors['O'] = competitors['O']+1

            if item[position] == 'front':
                competitors['b'] = competitors['b']+1
                competitors['p'] = competitors['p']+1
                competitors['m'] = competitors['m']+1
                competitors['v'] = competitors['v']+1
                competitors['f'] = competitors['f']+1
                competitors['l'] = competitors['l']+1
                competitors['e'] = competitors['e']+1
                competitors['E'] = competitors['E']+1
                competitors['i'] = competitors['i']+1

            if item[position] == 'middle':
                competitors['d'] = competitors['d']+1
                competitors['t'] = competitors['t']+1
                competitors['n'] = competitors['n']+1
                competitors['z'] = competitors['z']+1
                competitors['s'] = competitors['s']+1
                competitors['r'] = competitors['r']+1
                competitors['a'] = competitors['a']+1

            if item[position] == 'back':
                competitors['g'] = competitors['g']+1
                competitors['k'] = competitors['k']+1
                competitors['j'] = competitors['j']+1
                competitors['x'] = competitors['x']+1
                competitors['o'] = competitors['o']+1
                competitors['O'] = competitors['O']+1
                competitors['u'] = competitors['u']+1

            if item[position] == 'd1':
                competitors['d'] = competitors['d']+1
                competitors['b'] = competitors['b']+1
                competitors['g'] = competitors['g']+1
                competitors['m'] = competitors['m']+1
                competitors['v'] = competitors['v']+1
                competitors['z'] = competitors['z']+1
                competitors['j'] = competitors['j']+1
                competitors['l'] = competitors['l']+1
                competitors['o'] = competitors['o']+1
                competitors['n'] = competitors['n']+1
                competitors['r'] = competitors['r']+1
                competitors['e'] = competitors['e']+1
            if item[position] == 'd2':
                competitors['p'] = competitors['p']+1
                competitors['t'] = competitors['t']+1
                competitors['k'] = competitors['k']+1
                competitors['f'] = competitors['f']+1
                competitors['s'] = competitors['s']+1
                competitors['x'] = competitors['x']+1
                competitors['a'] = competitors['a']+1
                competitors['E'] = competitors['E']+1
                competitors['i'] = competitors['i']+1
                competitors['O'] = competitors['O']+1
                competitors['u'] = competitors['u']+1

    winner_score = max(competitors.items(), key=lambda k: k[1])

    winner = str(winner_score[0])

    return winner


def decoding(vector2string):
    """
    Decode wickelfeatures.

    Given a list of wickelfeatures decodes it back into phonemes.

    :vector2string type: list
    :rtype: str
    """
    # decodes the first trigram, i.e, the first 3 symbols of a verb
    decoded = str(checkcandidates_beg(vector2string)['decoded'])

    # finds a new compatible list of wickelfeatures, i.e., an intersection with the first decoded trigram

    new_wicklftrs = find_compatible(checkcandidates_beg(vector2string)['wickelfeatures'], vector2string)

    while len(new_wicklftrs) > 16:

        # decodes the next phoneme
        phoneme = competition(new_wicklftrs, 2)

        # does this until last phoneme is decoded
        new_wicklftrs = find_compatible(new_wicklftrs, vector2string)

        # sums the new phoneme to the
        decoded = decoded + phoneme

    return decoded
