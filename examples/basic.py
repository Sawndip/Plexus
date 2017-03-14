import plexus
import time
from itertools import repeat
import random

SIZE = 256
INPUT_SIZE = 4
OUTPUT_SIZE = 2
CONNECTIVITY = 0.1
PRECISION = 1

TRAINING_DURATION = 3

def generate_list_bigger():
    generated_list = []
    for i in repeat(None, 4):
        generated_list.append(round(random.uniform(0.6, 1.0), PRECISION))
    return generated_list

def generate_list_smaller():
    generated_list = []
    for i in repeat(None, 4):
        generated_list.append(round(random.uniform(0.0, 0.4), PRECISION))
    return generated_list


print "\n___ PLEXUS NETWORK BASIC EXAMPLE ___\n"

print "Create a Plexus network with " + str(SIZE) + " neurons, " + str(INPUT_SIZE) + " of them sensory, " + str(OUTPUT_SIZE) + " of them cognitive, " + str(CONNECTIVITY) + " connectivity rate, " + str(PRECISION) + " digit precision"
net = plexus.Network(SIZE,INPUT_SIZE,OUTPUT_SIZE,CONNECTIVITY,PRECISION)

print "\n*** LEARNING ***"

print "\nGenerate The Dataset (10 Items Long) To Classify The Numbers Bigger Than 0.5 & Learn for " + str(TRAINING_DURATION) + " Seconds Each"
for i in repeat(None, 10):
    generated_list = generate_list_bigger()
    print "Load Input: " + str(generated_list) + "\tOutput: [1.0, 0.0]\tand wait " + str(TRAINING_DURATION) + " seconds"
    net.load(generated_list, [1.0, 0.0])
    time.sleep(TRAINING_DURATION)

print "\nGenerate The Dataset (10 Items Long) To Classify The Numbers Smaller Than 0.5 & Learn for " + str(TRAINING_DURATION) + " Seconds Each"
for i in repeat(None, 10):
    generated_list = generate_list_smaller()
    print "Load Input: " + str(generated_list) + "\tOutput: [0.0, 1.0]\tand wait " + str(TRAINING_DURATION) + " seconds"
    net.load(generated_list, [0.0, 1.0])
    time.sleep(TRAINING_DURATION)

print "\n\n*** TESTING ***"

print "\nGenerate Test Data (10 Times) With The Numbers Bigger Than 0.5"
for i in repeat(None, 10):
    generated_list = generate_list_bigger()
    print "Load Input: " + str(generated_list) + "\tExpected: [1.0, 0.0]"
    net.load(generated_list)
    time.sleep(TRAINING_DURATION)

print "\nGenerate Test Data (10 Times) With The Numbers Smaller Than 0.5"
for i in repeat(None, 10):
    generated_list = generate_list_smaller()
    print "Load Input: " + str(generated_list) + "\tExpected: [0.0, 1.0]"
    net.load(generated_list)
    time.sleep(TRAINING_DURATION)

print "\n"
net.freeze()

#print ""
#for neuron in net.neurons:
#    print "A type " + str(neuron.type) + " neuron fired " + str(neuron.fire_counter) + " times"
#print ""

print "\n" + str(net.wave_counter) + " waves are executed throughout the network"

print "\nIn total: " + str(net.fire_counter) + " times a random non-sensory neuron fired\n"

print "Exit the program"
