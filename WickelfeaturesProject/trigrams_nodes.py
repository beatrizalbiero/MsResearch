import pickle
with open("trigrams.txt", "rb") as fp:   # Unpickling
        trigrams_dict = pickle.load(fp)
        trigrams_dict.sort()
