###############################################################################
"""
Coding Function.

The coding function receives a string (in this case, a verb)
and returns a boolean list with length 460, which is going to be the
activation vector after all.
"""
###############################################################################

from itertools import islice, tee
from itertools import compress
from Files import dct
from Files import nodes


def dataTest(phoneticinf, phoneticI):
    """
    Check dataset.

    A function to test if the dataset fits the network's requirements.

    :type phoneticinf: list
    :type phoneticI: list
    :rtype: str
    """
    i = 1
    for word in phoneticinf:
        if str(word[0]) != '#':
            print('error: # missing in line {}'.format(i))
            break
        else:
            i = i + 1
        i = 1
        for letter in word:
            if str(letter) not in dct.dictio:
                print('error: char ' + letter +
                      ' not in dictionary in word:' + word + ' line ' + str(i))
                break
    i = 1
    for word in phoneticI:
        if str(word[0]) != '#':
            print('error: # missing in line {}'.format(i))
            break
        else:
            i = i + 1
        i = 1
        for character in word:
            if str(character) not in dct.dictio:
                print('error: char ' + character +
                      ' not in dictionary in word:' + word + ' line ' + str(i))
                break

    return 'done'


def trigramizer(verb):
    """
    Trigramizer.

    This procedure receives a verb and returns a list of all trigrams.

    :type verb: str
    :rtype: list
    """
    N = 3
    trigrams = zip(*(islice(seq, index, None) for index, seq in enumerate(tee(verb, N))))
    return list(trigrams)


def create_matrix(trigrams_list):
    """
    Create a matrix.

    This procedure receives a trigram of phonemes and returns,
    (for a single trigram), a list of its phonemes associated to the dictionary

    :trigrams_list type: list
    :rtype: list
    """
    matrix = []
    for lst in trigrams_list:
        trigram_list = []
        for i in lst:
            trigram_list.append(dct.dictio[i])
        matrix.append(trigram_list)
    return matrix


def wickelfeatures(verb):
    """
    Wickelfeatures.

    Given a verb, this procedure returns a matrix of Wickelfeatures, i.e.,
     trigrams associated to the dicionary of features

    :verb type: str
    :rtype: list
    """
    trig = trigramizer(verb)
    matrix = create_matrix(trig)

    return matrix


"""
A list of 460 nodes (wickelfeatures) has been created so we can compare it to
the verb wikelfeatures.
"""
wickelfeatures_list = nodes.nds


def prep(lista_wkl):
    """
    Prep: Prepares the verb for the comparison.

    This procedure receives a single wickelfeature and
    returns a table of 16 wickelfeatures that are going to be activated
    (based on McClellands and Rumelharts experiment)
    Selects the wickelfeatures that are going to be activated by each trigram

    :lista_wkl type: list
    :rtype: list
    """
    new_list = [
                [lista_wkl[0][0], lista_wkl[1][0], lista_wkl[2][0]],
                [lista_wkl[0][1], lista_wkl[1][0], lista_wkl[2][1]],
                [lista_wkl[0][2], lista_wkl[1][0], lista_wkl[2][2]],
                [lista_wkl[0][3], lista_wkl[1][0], lista_wkl[2][3]],
                [lista_wkl[0][0], lista_wkl[1][1], lista_wkl[2][0]],
                [lista_wkl[0][1], lista_wkl[1][1], lista_wkl[2][1]],
                [lista_wkl[0][2], lista_wkl[1][1], lista_wkl[2][2]],
                [lista_wkl[0][3], lista_wkl[1][1], lista_wkl[2][3]],
                [lista_wkl[0][0], lista_wkl[1][2], lista_wkl[2][0]],
                [lista_wkl[0][1], lista_wkl[1][2], lista_wkl[2][1]],
                [lista_wkl[0][2], lista_wkl[1][2], lista_wkl[2][2]],
                [lista_wkl[0][3], lista_wkl[1][2], lista_wkl[2][3]],
                [lista_wkl[0][0], lista_wkl[1][3], lista_wkl[2][0]],
                [lista_wkl[0][1], lista_wkl[1][3], lista_wkl[2][1]],
                [lista_wkl[0][2], lista_wkl[1][3], lista_wkl[2][2]],
                [lista_wkl[0][3], lista_wkl[1][3], lista_wkl[2][3]]
    ]
    return new_list


def activate_nodes(verb):
    """
    Activate nodes.

    This procedure receives a verb and returns a list of wickelfeatures to be
    activated (based in the 'prep' procedure).

    :verb type: str
    :rtype: list
    """
    list_prep = []
    for item in wickelfeatures(verb):
        list_prep.append(prep(item))
    return list_prep


def compare(list1, list2):
    """
    Compare two lists.

    This procedure simply compares a list of wickelfeatures (of the required
    verb) with the table of all possible wickelfeatures (the
    wickelfeatures_list)
    It is a boolean vector with length 460.

    :list1 type: list
    :list2 type: list
    :rtype: list
    """
    list_i = [0] * 460
    for item in list2:
        for x in item:
            for i, element in enumerate(list1):
                if(x == element):
                    list_i[i] = 1

    return list_i


def coding(verb,coded=True,verbose=False):
    """
    coding.

    Finally, this procedure receives a verb and returns a 460 length boolean
    list.

    :verb type: str
    :rtype: list
    """
    def vector2string(filter_list, wickelfeatures_list):
        """
        vector2string.

        This procedure receives a boolean list of wickelfeatures and returns a
        string vector of wickelfeatures.

        :filter_list type: list
        :wickelfeatures_list type: list
        :rtype: list
        """
        vecting = list(compress(wickelfeatures_list, filter_list))
        return vecting
    table = activate_nodes(verb)
    nodes = compare(wickelfeatures_list, table)
    if coded is False and verbose is True:
        return vector2string(nodes,wickelfeatures_list)  # returns a list of wickelfeatures
    elif coded is True and verbose is False:
        return nodes  # returns a list of nodes
    elif coded is True and verbose is True:
        for i in range(0, 460):
            if nodes[i] == 1:
                print(wickelfeatures_list[i], ", value: ", nodes[i])
        return "done"
    else:
        return "one parameter must be set True"


# Example:
dar = coding("#dar#")
