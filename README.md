# README

# Project Summary

This is an attempt at reproducing Rumelhart and McClelland's (1986) connectionist experiment described  in the book Paralell Distributed Processing, chapter "On learning the past tense of English verbs", with Brazilian Portuguese as a target language.

In this book, Rumelhart and McClelland describe a new theory of cognition called connectionism that is challenging the idea of symbolic computation that has traditionally been at the center of debate in theoretical discussions about the mind.

The authors' theory assumes the mind is composed of a great number of elementary units connected in a neural network. Mental processes are interactions between these units which excite and inhibit each other in parallel rather than sequential operations. In this context, knowledge can no longer be thought of as stored in localized structures; instead, it consists of the connections between pairs of units that are distributed throughout the network.

In the chapter "On learning the past tense of English verbs", Rumelhart and McClelland describe an experiment in which a feedforward neural network was developed in order to find patterns among phonological features between present and past tense forms of English verbs.

# Wickelfeatures - Units

A phoneme can be described as any of the perceptually distinct units of sound in a specified language that distinguish one word from another, for example p, b, d, and t in the English words pad, pat, bad, and bat.

Each phoneme has its own phonological features. According to Rumelhart and McClelland's description, the phoneme 'd', for example, can be characterized by a set of 4 features (considering 4 different dimensions in a simplified phonetic table described by the authors):  

  - Interrupted
  - Stop
  - Middle
  - Voiced

|       |        |       |     | Place  |     |      |     |
|-------|--------|-------|-----|--------|-----|------|-----|
|       |        | Front |     | Middle |     | Back |     |
|       |        | V/L   | U/S | V/L    | U/S | V/L  | U/S |
| Int   | Stop   | b     | p   | d      | t   | g    | k   |
|       | Nasal  | m     | _   | n      | _   | N    | _   |
| Cont  | Fric   | v/D   | f/T | z      | s   | Z/j  | S/C |
|       | Liq/SV | w/l   | _   | r      | _   | y    | h   |
| Vowel | High   | E     | i   | O      | ^   | U    | u   |
|       | Low    | A     | e   | I      | a   | W    | o   |


In a trigram of phonemes, each phoneme may be ascribed 4 features. A Wickelfeature is a combination of 3 sequential features.

Rumelhart and McClelland used Wickelfeatures as input units for their neural network.

# The Corpus

All the necessary information about the corpus can be found [here](https://github.com/beatrizalbiero/MsResearch/tree/master/WickelfeaturesProject/Corpus).

# The Wickelfeatures Net

This is the net scheme that I've built to predict conjugations for Brazilian Portuguese. (present - first person)
<br/><br/>
![alt text](https://user-images.githubusercontent.com/31517216/32189712-ba7451a0-bd92-11e7-92fa-b332c58cc962.png)

# The Wickelfeatures Encoding Function

The [code](https://github.com/beatrizalbiero/MsResearch/blob/master/Project/coding_function.py) for how I've turned verbs into Wickelfeatures.

# The Decoding/Binding Function

The [code](https://github.com/beatrizalbiero/MsResearch/blob/master/Project/decoding2.py) for how I've tried to decode Wickelfeatures back into verbs.

# The Wickelfeatures Net

To build this [net](https://github.com/beatrizalbiero/MsResearch/blob/master/Project/network.py), I've used the API [KERAS](https://keras.io/)



# Jupyter Notebook of my net with premilinar results:

A preview of my experiments and results can be found [here](https://github.com/beatrizalbiero/MsResearch/blob/master/Project/Network.ipynb)!
