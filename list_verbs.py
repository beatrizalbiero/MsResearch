import pickle

list_verbs = ["#comer#",
"#beber#",
"#saber#",
"#caber#",
"#olhar#",
"#gostar#"]

with open("list_verbs.txt", "wb") as file:
     pickle.dump(list_verbs, file)
