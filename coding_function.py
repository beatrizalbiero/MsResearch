##############################################################################################################################
'''
Coding Function:
The coding function receives a string (in this case, a verb)
and returns a boolean list with length 460, which is going to be the activation vetor after all.
'''
##############################################################################################################################

import pickle
from itertools import islice, tee
from itertools import compress

def dictionary(phoneme):
    """
    dictionary
    This dictionary associates a phoneme to a set of phonological features
    This dictionary was created based on the phonological table of brazilian portuguese language

    :type phoneme: str
    :rtype: dict

    """

    dictio = {
             "#":["#","#","#","#","#"],
             "b":["int","b1","front","d1","notboundary"], "p":["int","b1","front","d2","notboundary"],
             "d":["int","b1","middle","d1","notboundary"],"t":["int","b1","middle","d2","notboundary"],
             "g":["int","b1","back","d1","notboundary"],"k":["int","b1","back","d2","notboundary"],
             "m":["int","b2","front","d1","notboundary"],"n":["int","b2","middle","d1","notboundary"],
             "v":["cont","b1","front","d1","notboundary"],"f":["cont","b1","front","d2","notboundary"],
             "z":["cont","b1","middle","d1","notboundary"],"s":["cont","b1","middle","d2","notboundary"],
             "j":["cont","b1","back","d1","notboundary"],"x":["cont","b1","back","d2","notboundary"],
             "l":["cont","b2","front","d1","notboundary"],"r":["cont","b2","middle","d1","notboundary"],
             "h":["cont","b2","back","d2","notboundary"],
             "a":["vowel","b2","middle","d2","notboundary"],"e":["vowel","b1","front","d1","notboundary"],
             "E":["vowel","b2","front","d2","notboundary"], "i":["vowel","b1","front","d2","notboundary"],
             "o":["vowel","b1","back","d1","notboundary"], "O":["vowel","b2","back","d2","notboundary"],
             "u":["vowel","b1","back","d2","notboundary"]
             }
    return dictio[phoneme]

def trigramizer(verb):
    """
    trigramizer
    This procedure receives a verb and returns a list of all trigrams

    :type verb: str
    :rtype: list
    """
    N = 3
    trigrams = zip(*(islice(seq, index, None) for index, seq in enumerate(tee(verb, N))))
    return list(trigrams)

def create_matrix(trigrams_list):
    """
    create_matrix
    This procedure receives a trigram of phonemes and returns, (for a single trigram), a list of its phonemes
    associated to the dictionary

    :trigrams_list type: list
    :rtype: list
    """
    matrix=[]
    for lst in trigrams_list:
        trigram_list = []
        for i in lst:
            trigram_list.append(dictionary(i))
        matrix.append(trigram_list)
    return matrix

def wickelfeatures(verb):
    """
    wickelfeatures
    Given a verb, this procedure returns a matrix of Wickelfeatures, i.e., trigrams associated to
    the dicionary of features

    :verb type: str
    :rtype: list
    """
    trig = trigramizer(verb)
    matrix = create_matrix(trig)

    return matrix

'''
Input nodes "dictionary"
A list of 460 nodes (wickelfeatures) has been created so we can compare it to the verb wikelfeatures
'''
with open("nodes.txt", "rb") as file:
    wickelfeatures_list = pickle.load(file)

def prep(lista_wkl):
    """
    Prep: Prepares the verb for the comparison
    This procedure receives a single wickelfeature and
    returns a table of 16 wickelfeatures that are going to be activated
    (based on McClellands and Rumelharts experiment)
    Selects the wickelfeatures that are going to be activated by each trigram

    :lista_wkl type: list
    :rtype: list
    """
    new_list = [
    [lista_wkl[0][0], lista_wkl[1][0],lista_wkl[2][0]],
    [lista_wkl[0][1], lista_wkl[1][0],lista_wkl[2][1]],
    [lista_wkl[0][2], lista_wkl[1][0],lista_wkl[2][2]],
    [lista_wkl[0][3], lista_wkl[1][0],lista_wkl[2][3]],
    [lista_wkl[0][0], lista_wkl[1][1],lista_wkl[2][0]],
    [lista_wkl[0][1], lista_wkl[1][1],lista_wkl[2][1]],
    [lista_wkl[0][2], lista_wkl[1][1],lista_wkl[2][2]],
    [lista_wkl[0][3], lista_wkl[1][1],lista_wkl[2][3]],
    [lista_wkl[0][0], lista_wkl[1][2],lista_wkl[2][0]],
    [lista_wkl[0][1], lista_wkl[1][2],lista_wkl[2][1]],
    [lista_wkl[0][2], lista_wkl[1][2],lista_wkl[2][2]],
    [lista_wkl[0][3], lista_wkl[1][2],lista_wkl[2][3]],
    [lista_wkl[0][0], lista_wkl[1][3],lista_wkl[2][0]],
    [lista_wkl[0][1], lista_wkl[1][3],lista_wkl[2][1]],
    [lista_wkl[0][2], lista_wkl[1][3],lista_wkl[2][2]],
    [lista_wkl[0][3], lista_wkl[1][3],lista_wkl[2][3]]
    ]
    return new_list

def activate_nodes(verb): #for each verb, returns the table of features to be activated
    """
    activate_nodes
    This procedure receives a verb and returns a list of wickelfeatures to be activated (based in the 'prep' procedure)

    :verb type: str
    :rtype: list
    """
    list_prep = []
    for item in wickelfeatures(verb):
        list_prep.append(prep(item))
    return list_prep

def compare (list1,list2):
    """
    compare
    This procedure simply compares a list of wickelfeatures (of the required verb) with the table of all
    possible wickelfeatures (the wickelfeatures_list)
    It is a boolean vector with length 460.

    :list1 type: list
    :list2 type: list
    :rtype: list
    """
    list_i =[0]*460
    for item in list2:
        for x in item:
            for i, element in enumerate(list1):
                if(x == element):
                    list_i[i] = 1

    return list_i

def coding(verb):
    """
    coding
    Finally, this procedure receives a verb and returns a 460 length boolean list.

    :verb type: str
    :rtype: list
    """
    table = activate_nodes(verb)
    nodes = compare(wickelfeatures_list,table)
    return nodes

#Example:
dar = coding("#dar#")

def vector2string(filter_list,wickelfeatures_list):
    '''
    vector2string
    This procedure receives a boolean list of wickelfeatures and returns a string vector of wickelfeatures

    :filter_list type: list
    :wickelfeatures_list type: list
    :rtype: list
    '''
    vecting = list(compress(wickelfeatures_list, filter_list))
    return vecting
