import coding_function as cf
import csv

'''
open a csv file containing phonetic transcribed verbs, inifitive and conjugated forms
'''
with open('ptverbs_test.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
    phoneticinf = []
    phoneticI = []

    for row in readcsv:
        phinf = row[1]
        phI = row[3]
        phoneticinf.append(phinf)
        phoneticI.append(phI)


'''
create two dictionaries, one for inifitive forms and another for conjugated forms
'''

dictioinf = {}
dictioI = {}

for item in phoneticinf:
    dictioinf[item] = cf.coding(item)

for item in phoneticI:
    dictioI[item] = cf.coding(item)

dictioinf.values()
dictioI
