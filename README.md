# README

# Project Summary

This is an attempt at reproducing Rumelhart and McClelland's (1986) connectionist experiment described  in the book Paralell Distributed Processing, chapter "On learning the past tense of English verbs", with Brazilian Portuguese as a target language.

In this book, Rumelhart and McClelland describe a new theory of cognition called connectionism that is challenging the idea of symbolic computation that has traditionally been at the center of debate in theoretical discussions about the mind.

The authors' theory assumes the mind is composed of a great number of elementary units connected in a neural network. Mental processes are interactions between these units which excite and inhibit each other in parallel rather than sequential operations. In this context, knowledge can no longer be thought of as stored in localized structures; instead, it consists of the connections between pairs of units that are distributed throughout the network.

In the chapter "On learning the past tense of English verbs", Rumelhart and McClelland describe an experiment in which a feedforward neural network was developed in order to find patterns among phonological features between present and past tense forms of English verbs.

# The Corpus 

All the necessary information about the corpus can be found [here](https://github.com/beatrizalbiero/MsResearch/tree/master/WickelfeaturesProject/Corpus).

**TODO:** Update information about the new Corpus.

# The Wickelfeatures Net

This is the net scheme that I've built to predict conjugations for Brazilian Portuguese. (present - first person)
In this net, I've used the same network architecture as researchers Rumelhart and McClelland did.
<br/><br/>
![alt text](https://user-images.githubusercontent.com/31517216/32189712-ba7451a0-bd92-11e7-92fa-b332c58cc962.png)

To build this [net](https://github.com/beatrizalbiero/MsResearch/blob/master/WickelfeaturesProject/Network.ipynb), I've used the API [KERAS](https://keras.io/)

# Encoder-Decoder

I'm currently studying the same task with an [encoder-decoder](https://github.com/beatrizalbiero/MsResearch/blob/master/input_features.ipynb) architecture.
