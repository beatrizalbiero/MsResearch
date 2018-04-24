class decoded:
    import pickle
    import coding_function as cf
    import decoding_function as df
    with open("nodes.txt", "rb") as file:
        wickelfeatures_list = pickle.load(file)
    def __init__(self,vector):
        self.vector = vector
        self.wickel = False
        self.decoded = False
        def vec2str(self):
            self.wickel = cf.vector2string(self.vector,wickelfeatures_list)
            return print(self.wickel)
        def decode(self):
            self.decoded = df.decoding(self.wickel)
            return True
