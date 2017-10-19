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

In a trigram of phonemes, each phoneme may be ascribed 4 features in each dimension allowing for 64 possible combinations. A Wickelfeature is any one of those combinations. 

Rumelhart and McClelland used Wickelfeatures as input units for their neural network.

# The Neural Net 

![Alt text](/Users/Beatriz/Dropbox/Linguística/algoritmos/principal/neuralnet.jpg)


# Folders 
 - coding_function
 - decoding_function
 - wickelfeatures_inputs_generator
 - list_verbs
 
# TODO
- phonetic transcription of verbs
- finish the decoding function
- neural networks
- (...)
