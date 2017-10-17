'''
Decoding function:
After the neural network training, there must be a way of converting a vector of wickelfeatures into wickelphones again and, finally,
back to a whole string (verb).
'''
##############################################################################################################################################################

import coding_function as cf
#importlib.reload(cf)
import pickle
with open("nodes.txt", "rb") as file:
    wickelfeatures_list = pickle.load(file)

##############################################################################################################################################################

'''
idea: start with a set of possible candidates and then reducing them until we have a winner
MyList: A new class develop in order to eliminate incompatibilities
'''

class MyList(list):
    def __init__(self, *args):
        super(MyList, self).__init__(args)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])

##############################################################################################################################################################

'''
A procedure that decodes the first trigram of a verb THIS MIGHT BE USELESS
'''

def checkcandidates_beg(vector2string):
    candidates1 = MyList('b','p','d','t','g',
                'k','m','n','v','f','z','s',
                'j','x','l','r','a','e','E',
                'i', 'o', 'O', 'u')
    candidates2 = MyList('b','p','d','t','g',
                'k','m','n','v','f','z','s',
                'j','x','l','r','a','e','E',
                'i', 'o', 'O', 'u')

    ints = MyList('b','p','d','t','g','k','m','n')
    conts = MyList('v','f','z','s','j','x','l','r')
    vowels = MyList('a','e','E','i', 'o', 'O', 'u')
    b1s = MyList('b','p','d','t','g','k','v','f','z','s','j','x','e','i','o','u')
    b2s = MyList('m','n','l','r','a','E','O')
    fronts = MyList('b','p','v','f','m','l','E','i','e')
    middles = MyList('d','t','n','z','s','r','a')
    backs = MyList('g','k','j','x','o', 'O', 'u')
    d1s = MyList('b','d','g','m','v','z','j','l','o','n','r','e')
    d2s = MyList('p', 't', 'k', 'f', 's', 'x', 'a', 'E', 'O', 'u','i')

    new = []

    for item in vector2string:
        if item[0] == '#':
            new.append(item)
            if item[1] == 'int':
                #print(candidates)
                candidates1 = candidates1 - conts - vowels
            if item[1] == 'cont':
                candidates1 = candidates1 - ints - vowels
            if item[1] == 'vowel':
                #print(candidates)
                candidates1 = candidates1 - conts - ints
            if item[1] == 'b1':
                #print(candidates)
                candidates1 = candidates1 - b2s
            if item[1] == 'b2':
                #print(candidates)
                candidates1 = candidates1 - b1s
            if item[1] == 'front':
                #print(candidates)
                candidates1 = candidates1 - middles - backs
            if item[1] == 'middle':
                #print(candidates)
                candidates1 = candidates1 - fronts - backs
            if item[1] == 'back':
                #print(candidates)
                candidates1 = candidates1 - fronts - middles
            if item[1] == 'd1':
                #print(candidates)
                candidates1 = candidates1 - d2s
            if item[1] == 'd2':
                #print(candidates)
                candidates1 = candidates1 - d1s
            if item[2] == 'int':
                #print(candidates)
                candidates2 = candidates2 - conts - vowels
            if item[2] == 'cont':
                candidates2 = candidates2 - ints - vowels
            if item[2] == 'vowel':
                #print(candidates)
                candidates2 = candidates2 - conts - ints

            if item[2] == 'b1':
                #print(candidates)
                candidates2 = candidates2 - b2s

            if item[2] == 'b2':
                #print(candidates)
                candidates2 = candidates2 - b1s
            if item[2] == 'front':
                #print(candidates)
                candidates2 = candidates2 - middles - backs
            if item[2] == 'middle':
                #print(candidates)
                candidates2 = candidates2 - fronts - backs
            if item[2] == 'back':
                #print(candidates)
                candidates2 = candidates2 - fronts - middles

            if item[2] == 'd1':
                #print(candidates)
                candidates2 = candidates2 - d2s

            if item[2] == 'd2':
                #print(candidates)
                candidates2 = candidates2 - d1s


    return {'decoded': "".join(['#'] + candidates1 + candidates2), 'wickelfeatures':new}


checkcandidates_beg(Dar)['decoded']
type(checkcandidates_beg(Dar)['decoded'])
##############################################################################################################################################
'''
A procedure that decodes the last trigram
'''
##############################################################################################################################################################

def checkcandidates_end(vector2string):

    candidates1 = MyList('b','p','d','t','g',
                        'k','m','n','v','f','z','s',
                        'j','x','l','r','a','e','E',
                        'i', 'o', 'O', 'u')

    candidates2 = MyList('b','p','d','t','g',
                        'k','m','n','v','f','z','s',
                        'j','x','l','r','a','e','E',
                        'i', 'o', 'O', 'u')
    ints = MyList('b','p','d','t','g','k','m','n')
    conts = MyList('v','f','z','s','j','x','l','r')
    vowels = MyList('a','e','E','i', 'o', 'O', 'u')
    b1s = MyList('b','p','d','t','g','k','v','f','z','s','j','x','e','i','o','u')
    b2s = MyList('m','n','l','r','a','E','O')
    fronts = MyList('b','p','v','f','m','l','E','i','e')
    middles = MyList('d','t','n','z','s','r','a')
    backs = MyList('g','k','j','x','o', 'O', 'u')
    d1s = MyList('b','d','g','m','v','z','j','l','o','n','r','e')
    d2s = MyList('p', 't', 'k', 'f', 's', 'x', 'a', 'E', 'O', 'u','i')

    for item in vector2string:

        if item[2] == '#':
            if item[0] == 'int':
                #print(candidates)
                candidates1 = candidates1 - conts - vowels
            if item[0] == 'cont':
                print("entrei")
                candidates1 = candidates1 - ints - vowels
            if item[0] == 'vowel':
                #print(candidates)
                candidates1 = candidates1 - conts - ints
            if item[0] == 'b1':
                #print(candidates)
                candidates1 = candidates1 - b2s
            if item[0] == 'b2':
                #print(candidates)
                candidates1 = candidates1 - b1s
            if item[0] == 'front':
                #print(candidates)
                candidates1 = candidates1 - middles - backs
            if item[0] == 'middle':
                #print(candidates)
                candidates1 = candidates1 - fronts - backs
            if item[0] == 'back':
                #print(candidates)
                candidates1 = candidates1 - fronts - middles
            if item[0] == 'd1':

                candidates1 = candidates1 - d2s
            if item[0] == 'd2':

                candidates1 = candidates1 - d1s
            if item[1] == 'int':

                candidates2 = candidates2 - conts - vowels
            if item[1] == 'cont':
                candidates2 = candidates2 - ints - vowels
            if item[1] == 'vowel':
                candidates2 = candidates2 - conts - ints
            if item[1] == 'b1':

                candidates2 = candidates2 - b2s

            if item[1] == 'b2':
                #print(candidates)
                candidates2 = candidates2 - b1s
            if item[1] == 'front':
                #print(candidates)
                candidates2 = candidates2 - middles - backs
            if item[1] == 'middle':
                #print(candidates)
                candidates2 = candidates2 - fronts - backs
            if item[1] == 'back':
                #print(candidates)
                candidates2 = candidates2 - fronts - middles

            if item[1] == 'd1':
                #print(candidates)
                candidates2 = candidates2 - d2s

            if item[1] == 'd2':
                #print(candidates)
                candidates2 = candidates2 - d1s



    return "".join(candidates1 + candidates2 + ["#"])

#checkcandidates_end(Comer)

# hidden smallbinding#############################################################################################################################################################
# '''
# A procedure that decodes a whole verb if there are less than 4 letters in it:
# '''
# dar = cf.coding("#dar#")
# def smallbinding(coded_verb): #receives a coded verb, i.e., a boolean vector representing a verb
#     if coded_verb.count(1) < 49:
#         Verb = cf.vector2string(coded_verb,wickelfeatures_list)
#         beg = checkcandidates_beg(Verb)
#         #print(beg)
#         end = checkcandidates_end(Verb)
#         return beg[0]+beg[1]+end[1]
#     else:
#         return print('Error: big verb')
#
# smallbinding(dar)
##############################################################################################################################################
import random
################
# '''
# checkcandidate
# given a set of wickelfeatures and a position(integer) in the trigram, returns a phoneme candidate
# '''
# def checkcandidate(vector2string,position):
#
#     '''
#     REMINDER:
#     THIS FUNCTION MUST RECEIVE A SET OF WICKELFEATURES REGARDING A SINGLE TRIGRAM.
#     '''
#
#     candidates = MyList('b','p','d','t','g','k','m','n','v','f','z','s','j','x','l','r','a','e','E','i', 'o', 'O', 'u')
#
#     ints = MyList('b','p','d','t','g','k','m','n')
#     conts = MyList('v','f','z','s','j','x','l','r')
#     vowels = MyList('a','e','E','i', 'o', 'O', 'u')
#     b1s = MyList('b','p','d','t','g','k','v','f','z','s','j','x','e','i','o','u')
#     b2s = MyList('m','n','l','r','a','E','O')
#     fronts = MyList('b','p','v','f','m','l','E','i','e')
#     middles = MyList('d','t','n','z','s','r','a')
#     backs = MyList('g','k','j','x','o', 'O', 'u')
#     d1s = MyList('b','d','g','m','v','z','j','l','o','n','r','e')
#     d2s = MyList('p', 't', 'k', 'f', 's', 'x', 'a', 'E', 'O', 'u','i')
#
#     for item in vector2string:
#         if item[position] == '#':
#             pass
#         else:
#             if item[position] == 'int':
#                 #print(candidates)
#                 candidates = candidates - conts - vowels
#             if item[position] == 'cont':
#                 candidates = candidates - ints - vowels
#             if item[position] == 'vowel':
#                 candidates = candidates - conts - ints
#                 #print(type(candidates))
#             if item[position] == 'b1':
#                 #print(candidates)
#                 candidates = candidates - b2s
#             if item[position] == 'b2':
#                 #print(candidates)
#                 candidates = candidates - b1s
#             if item[position] == 'front':
#                 #print(candidates)
#                 candidates = candidates - middles - backs
#             if item[position] == 'middle':
#                 #print(candidates)
#                 candidates = candidates - fronts - backs
#             if item[position] == 'back':
#                 #print(candidates)
#                 candidates = candidates - fronts - middles
#             if item[position] == 'd1':
#                 #print(candidates)
#                 candidates = candidates - d2s
#             if item[position] == 'd2':
#                 #print(candidates)
#                 candidates = candidates - d1s
#     return candidates[0]
#
# '''
# Usage:
# '''
# da = cf.coding('#da') #first, string into vector
# Da = cf.vector2string(da,wickelfeatures_list)
# Da #then, vector back to string
# type(checkcandidate(Da,0))
#

##############################################################################################################################################

'''
find_compatible:
i'm gonna compare the first decoded wickelfeatures with a list of possible new wickelfeatures, this procedure filters possible
candidates for the second trigram
'''

def find_compatible(list1,list2): #returns a list if compatible lists in list2 according to list1
    compatible =[]
    for item1 in list1:
        for item2 in list2:
            if item1[1] == item2[0] and item1[2] == item2[1]:
                compatible.append(item2)

    return compatible
##############################################################################################################################################

'''
competion of phonemes
'''
def competion(vector2string,position):
    competitors = {"b":0,"p":0,"d":0,'t':0,'g':0,'k':0,'m':0,'n':0,'v':0,'f':0,'z':0,'s':0,'j':0,'x':0,'l':0,
                    'r':0,'a':0,'e':0,'E':0,'i':0, 'o':0, 'O':0, 'u':0, '#':0}

    for item in vector2string:
            if item[position] == '#':
                competitors['#'] =+1

            if item[position] == 'int':
                competitors['b'] =+1
                competitors['p'] =+1
                competitors['d'] =+1
                competitors['t'] =+1
                competitors['g'] =+1
                competitors['k'] =+1
                competitors['m'] =+1
                competitors['n'] =+1

            if item[position] == 'cont':
                competitors['v'] =+1
                competitors['f'] =+1
                competitors['z'] =+1
                competitors['s'] =+1
                competitors['j'] =+1
                competitors['x'] =+1
                competitors['l'] =+1
                competitors['r'] =+1

            if item[position] == 'vowel':
                competitors['a'] =+1
                competitors['e'] =+1
                competitors['E'] =+1
                competitors['i'] =+1
                competitors['O'] =+1
                competitors['u'] =+1
                competitors['o'] =+1

            if item[position] == 'b1':
                competitors['b'] =+1
                competitors['p'] =+1
                competitors['d'] =+1
                competitors['t'] =+1
                competitors['g'] =+1
                competitors['k'] =+1
                competitors['v'] =+1
                competitors['f'] =+1
                competitors['z'] =+1
                competitors['s'] =+1
                competitors['j'] =+1
                competitors['x'] =+1
                competitors['e'] =+1
                competitors['i'] =+1
                competitors['u'] =+1
                competitors['o'] =+1

            if item[position] == 'b2':
                competitors['m'] =+1
                competitors['n'] =+1
                                
            if item[position] == 'front':
                #print(candidates)
                candidates = candidates - middles - backs
            if item[position] == 'middle':
                #print(candidates)
                candidates = candidates - fronts - backs
            if item[position] == 'back':
                #print(candidates)
                candidates = candidates - fronts - middles
            if item[position] == 'd1':
                #print(candidates)
                candidates = candidates - d2s
            if item[position] == 'd2':
                #print(candidates)
                candidates = candidates - d1s

    return winner

'''
decoding:
given a list of wickelfeatures (str), decodes it back into phonemes
'''
def decoding(vector2string): #a list of all wickelfeatures of a verb (strings)

    #decodes the first trigram, i.e, the first 3 symbols of a verb
    decoded = str(checkcandidates_beg(vector2string)['decoded'])

    #finds a new compatible list of wickelfeatures, i.e., an intersection with the first decoded trigram
    new_list_of_wickelfeatures = find_compatible(checkcandidates_beg(vector2string)['wickelfeatures'],vector2string)

    while len(new_list_of_wickelfeatures) > 16:

        #decodes the next phoneme
        phoneme = checkcandidate(new_list_of_wickelfeatures,2)

        #do this until last phoneme is decoded
        new_list_of_wickelfeatures = find_compatible(new_list_of_wickelfeatures,vector2string)

        #sums the new phoneme to the
        decoded = decoded + phoneme


    return decoded

dar = cf.coding('#dar#') #first, string into vector
Dar = cf.vector2string(dar,wickelfeatures_list)
new_list_of_wickelfeatures = find_compatible(checkcandidates_beg(Dar)['wickelfeatures'],Dar)
new_list_of_wickelfeatures
phoneme = checkcandidate(new_list_of_wickelfeatures,2)
phoneme
new_list_of_wickelfeatures = find_compatible(new_list_of_wickelfeatures,Dar)
new_list_of_wickelfeatures

find_compatible(checkcandidates_beg(Dar)['wickelfeatures'],Dar)

type(checkcandidates_beg(Dar)['wickelfeatures'])
type(Dar)

checkcandidates_beg(Dar)['wickelfeatures']

decoding(Dar)

phoneme = checkcandidate(new_list_of_wickelfeatures,1)
type(phoneme)
