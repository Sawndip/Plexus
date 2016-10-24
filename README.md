# Plexus

Plexus Network is the first object-oriented neural network, moreover, it's accelerated with multithreading.

<p align="center">
  <img src="https://raw.githubusercontent.com/mertyildiran/Plexus/master/docs/img/full.gif" alt="Plexus"/>
</p>

### Core Principles

These are the core principles of **exceptionally bio-inspired**, a revolutionary approach to the artificial neural networks:

 - **Neurons** must be **objects** not tensors between matrices.
 - Each neuron should have **its own thread**.
 - **Network** must be **architecture-free**, adaptive.
 - Network must have a **layerless design**.
 - There must be two types of neurons: **sensory neurons** and **interneurons**.
 - I/O of network must be made of sensory neurons.
 - There could be more than one input group (in old fashioned words: input layer), the same manner is true for the output.
 - Forget batch size, iteration, and epoch terms, training examples must be fed on time basis; *e.g. learn first sample for ten seconds, OK done? then learn second sample for twenty seconds*. By this approach, you can assign importance factors to your samples with maximum flexibility.
 - **Network** must be **retrainable**.
 - Network must be **modular**. In other words: You must be able to train this small network and then plug that network into a bigger network, we are talking about some kind of **self-fusing**.
 - Neurons must exhibit characteristics of **cellular automata**.
 - **Number of neurons** in network can be increased or decreased (**scalability**).
 - There must be **no** need for a network-wide **oscillation**.

### Version
0.0.6

### Installation

```Shell
sudo pip install plexus
```
